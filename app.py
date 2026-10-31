import os
import warnings
import streamlit as st
import joblib

# Suppress version mismatch warnings for pickled models
warnings.filterwarnings("ignore")

# Set Streamlit page configuration
st.set_page_config(
    page_title="Email Spam Detector",
    page_icon="📧",
    layout="centered"
)

# Load the trained model pipeline
@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "spam_model.pkl")
    return joblib.load(model_path)

try:
    model = load_model()
except Exception as e:
    st.error(f"Failed to load `spam_model.pkl`: {e}")
    st.stop()

# Initialize session state for text area
if "email_input_text" not in st.session_state:
    st.session_state.email_input_text = ""

def set_sample(text):
    st.session_state.email_input_text = text

def clear_input():
    st.session_state.email_input_text = ""

# Header
st.title("📧 Email / SMS Spam Detector")
st.markdown(
    "Detect whether an incoming email or text message is **Spam** or **Ham (Legitimate)** using machine learning."
)

st.divider()

# Sample texts
SAMPLE_HAM = "Hi team, please find the agenda attached for tomorrow's project review meeting at 10 AM. Let me know if you have any questions."
SAMPLE_SPAM_1 = "URGENT! You have won a 1,000,000 cash prize! Text CLAIM to 87121 immediately to claim your award. Offer expires today!"
SAMPLE_SPAM_2 = "URGENT: Your bank account has been suspended due to suspicious activity. Verify credentials now at http://bit.ly/fake-bank"

# Quick sample buttons
st.subheader("💡 Quick Test Samples")
col_s1, col_s2, col_s3 = st.columns(3)

sample_1 = col_s1.button(
    "📩 Meeting (Ham)",
    on_click=set_sample,
    args=(SAMPLE_HAM,),
    use_container_width=True
)
sample_2 = col_s2.button(
    "🎁 Lottery (Spam)",
    on_click=set_sample,
    args=(SAMPLE_SPAM_1,),
    use_container_width=True
)
sample_3 = col_s3.button(
    "💳 Account Alert (Spam)",
    on_click=set_sample,
    args=(SAMPLE_SPAM_2,),
    use_container_width=True
)

# Text input bound directly to session state via key
email_content = st.text_area(
    "Enter the email or message content:",
    height=160,
    placeholder="Type or paste the message here...",
    key="email_input_text"
)

# Action buttons
col_b1, col_b2 = st.columns([4, 1])
check_clicked = col_b1.button("🔍 Check Message", type="primary", use_container_width=True)
col_b2.button("🗑️ Clear", on_click=clear_input, use_container_width=True)

# Run classification when "Check Message" is clicked or when a sample button is pressed
if check_clicked or sample_1 or sample_2 or sample_3:
    content_to_check = st.session_state.email_input_text.strip()

    if not content_to_check:
        st.warning("⚠️ Please enter a message to classify.")
    else:
        # Prediction
        prediction = model.predict([content_to_check])[0]

        # Probabilities if supported by the model
        proba = None
        if hasattr(model, "predict_proba"):
            try:
                probabilities = model.predict_proba([content_to_check])[0]
                classes = list(model.classes_)
                if "spam" in classes:
                    spam_idx = classes.index("spam")
                    spam_conf = probabilities[spam_idx] * 100
                    ham_conf = 100 - spam_conf
                    proba = (ham_conf, spam_conf)
            except Exception:
                proba = None

        st.markdown("### Result")
        is_spam = str(prediction).lower() == "spam" or prediction == 1

        if is_spam:
            st.error("🚨 **This message is classified as SPAM!**")
        else:
            st.success("✅ **This message is classified as HAM (Legitimate).**")

        if proba is not None:
            ham_conf, spam_conf = proba
            conf = spam_conf if is_spam else ham_conf
            st.write(f"**Confidence:** `{conf:.2f}%`")
            st.progress(int(conf))
