# PhishGuard AI

PhishGuard AI is an AI-powered phishing email detection Chrome extension that analyzes Gmail emails in real time using Machine Learning, NLP, Flask API, and trusted domain reputation scoring.

The project detects whether an email is:
- Safe
- Uncertain
- Suspicious
- High Risk Phishing

based on semantic email analysis and confidence scoring.

---

# Features

- Real-time Gmail phishing detection
- Machine Learning based email classification
- NLP preprocessing using TF-IDF
- Flask backend API
- Chrome browser extension integration
- Trusted domain reputation system
- Dynamic email scanning without page reload

---

# Technologies Used

- Python
- Flask
- Scikit-learn
- NLTK
- JavaScript
- Chrome Extension API

---

# How to Run

## 1. Clone Repository

```bash
git clone https://github.com/S-Manish-reddy/PhishGuard-AI.git
```

```bash
cd PhishGuard-AI/backend
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Flask Backend

```bash
python app.py
```

Backend will start at:

```text
http://127.0.0.1:5000
```

---

## 5. Load Chrome Extension

Open Chrome and go to:

```text
chrome://extensions/
```

- Enable Developer Mode
- Click "Load unpacked"
- Select the `extension` folder

---

## 6. Open Gmail

Go to:

```text
https://mail.google.com
```

Open any email.

The extension will automatically:
- scan the email
- send content to the ML backend
- display phishing risk prediction in real time

---

# Threat Levels

| Threat Level | Meaning |
|---|---|
| Safe Email | Email appears legitimate |
| Uncertain Email | Low confidence prediction |
| Suspicious Email | Potential phishing indicators detected |
| High Risk Phishing | Strong phishing characteristics detected |

---

# Notes

- Flask backend must remain running while using the extension.
- Large datasets are excluded from the repository due to GitHub size limitations.
- Pretrained model files are included for direct usage.

---

# Future Improvements

- Transformer-based NLP models (BERT/DistilBERT)
- URL analysis
- SPF/DKIM validation
- Sender reputation analysis
- Multi-browser support
