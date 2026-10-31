# 📧 Email / SMS Spam Detector

A machine learning web application that classifies email and SMS text messages as **Spam** or **Ham (Legitimate)** in real time using NLP and Scikit-Learn, with an interactive web UI built in Streamlit.

---

## ✨ Features

- **Real-Time Classification**: Instant prediction of whether an incoming message is Spam or Ham.
- **Confidence Score**: Displays prediction confidence percentage and visual progress indicator.
- **Quick Test Samples**: One-click preset samples for both legitimate and spam messages.
- **Clean Streamlit UI**: User-friendly design with clear inputs and error handling.

---

## 🛠️ Tech Stack

- **Python** (>= 3.10)
- **Streamlit**: Web interface and interactive components
- **Scikit-Learn**: TF-IDF Vectorization and Logistic Regression classification pipeline
- **Joblib**: Model serialization and loading

---

## 📁 Project Structure

```text
├── app.py              # Streamlit application UI and logic
├── spam_model.pkl      # Pre-trained ML pipeline (TF-IDF + Classifier)
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/sonukmandal123/Spam-Detection-ML.git
cd Spam-Detection-ML
```

### 2. Set Up Virtual Environment

**Windows:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
