# PhishGuard AI — Detailed Project Explanation

## Overview

PhishGuard AI is an AI-powered phishing email detection system developed as a cybersecurity and machine learning project. The project combines Natural Language Processing (NLP), Machine Learning, Flask API development, and Chrome Extension technologies to analyze Gmail emails in real time and classify them based on phishing risk.

The primary objective of the project is to detect potentially malicious phishing emails using semantic content analysis instead of relying only on static keyword matching.

The system works as a real-time Gmail browser extension that scans opened emails dynamically and sends the email content to a Flask backend API where the machine learning model predicts whether the email is safe, suspicious, or high-risk phishing.

---

# Problem Statement

Traditional phishing detectors often rely on:

* hardcoded keywords
* blocked domain lists
* simple rule-based systems

These systems fail when:

* phishing emails use natural language
* legitimate emails contain urgent wording
* attackers avoid obvious phishing keywords

To overcome these limitations, PhishGuard AI uses:

* NLP preprocessing
* semantic feature extraction
* machine learning classification
* domain reputation analysis

to improve phishing detection quality.

---

# Project Workflow

The complete workflow of the system is:

Gmail Email
↓
Chrome Extension Extracts Email Content
↓
Content Sent to Flask API
↓
Machine Learning Model Analyzes Email
↓
Prediction + Confidence Returned
↓
Extension Displays Threat Level

---

# Dataset Collection

Initially, multiple phishing and legitimate email datasets were explored and merged. However, inconsistent labels and noisy data caused poor prediction performance.

The final implementation uses a cleaner phishing email dataset containing:

* Safe Emails
* Phishing Emails

The dataset was used to train the machine learning classifier after preprocessing and cleaning.

---

# Dataset Preprocessing

The preprocessing pipeline was developed using Python and NLTK.

The following preprocessing steps were implemented:

* Lowercasing text
* Removing URLs
* Removing email addresses
* Removing punctuation
* Tokenization
* Stopword removal
* Duplicate removal
* Missing value handling

The cleaned email text was stored in a processed dataset for machine learning training.

---

# NLP and Feature Engineering

Machine learning models cannot directly understand raw text data.

To solve this problem, TF-IDF (Term Frequency–Inverse Document Frequency) vectorization was used.

TF-IDF converts email text into numerical feature vectors by identifying:

* important words
* suspicious phrases
* phishing-related patterns
* semantic frequency relationships

The project also used:

* unigram features
* bigram features
* sublinear TF scaling

to improve semantic understanding.

---

# Machine Learning Model

Multiple models were experimented with during development, including:

* Logistic Regression
* Random Forest Classifier
* Multinomial Naive Bayes

After experimentation and optimization:

* Random Forest achieved the best detection accuracy
* Multinomial Naive Bayes was used as a lightweight deployment alternative

The final trained model was saved using Joblib serialization.

The model predicts:

* Safe Email
* Suspicious Email
* High Risk Phishing

along with confidence scores.

---

# Domain Reputation System

A trusted domain reputation system was integrated to reduce false positives.

The system uses the Tranco Top Domains List containing trusted and legitimate domains.

When trusted domains are detected inside email content:

* phishing confidence is reduced
* safe confidence is improved

This hybrid approach combines:

* machine learning
* reputation analysis

which is similar to real-world cybersecurity detection systems.

---

# Flask Backend API

A Flask REST API was developed to serve the machine learning model.

The API:

* loads the trained model
* receives email text
* performs prediction
* returns JSON responses

Example API response:

{
"prediction": "Suspicious Email",
"confidence": 72.45
}

This backend acts as the communication bridge between the browser extension and the machine learning model.

---

# Chrome Extension Integration

A Chrome browser extension was developed using:

* JavaScript
* Chrome Extension APIs
* Content Scripts

The extension dynamically monitors Gmail pages and detects newly opened emails without requiring page reloads.

The extension:

* extracts email content
* sends it to the Flask API
* receives predictions
* displays threat-level banners

The extension supports:

* dynamic email scanning
* real-time predictions
* automatic rescanning
* visual risk indicators

---

# Threat Scoring System

Instead of binary classification, the system uses a threat-level scoring approach:

* Safe Email
* Uncertain Email
* Suspicious Email
* High Risk Phishing

This improves usability and reduces misleading predictions.

The scoring logic is based on:

* machine learning confidence
* domain reputation signals

---

# Technologies Used

## Programming Languages

* Python
* JavaScript

## Backend

* Flask
* Flask-CORS

## Machine Learning

* Scikit-learn
* TF-IDF Vectorizer
* Random Forest
* Multinomial Naive Bayes

## NLP

* NLTK

## Frontend / Extension

* Chrome Extension API
* Content Scripts

---

# Challenges Faced

Several real-world challenges were encountered during development:

* Inconsistent dataset labels
* Noisy phishing datasets
* False positives on legitimate bank emails
* Semantic overlap between phishing and safe emails
* Large model sizes
* Extension CORS issues
* Dynamic Gmail content handling

These challenges were solved through:

* dataset cleaning
* preprocessing optimization
* reputation-based scoring
* confidence threshold tuning
* dynamic Gmail monitoring

---

# Future Improvements

Possible future enhancements include:

* Transformer-based NLP models (BERT/DistilBERT)
* URL and attachment analysis
* SPF/DKIM email validation
* Sender reputation analysis
* LLM-assisted phishing detection
* Cloud deployment
* Multi-browser support

---

# Conclusion

PhishGuard AI demonstrates how machine learning, NLP, browser extensions, and cybersecurity concepts can be combined to create a real-time phishing detection system.

The project provides practical experience in:

* cybersecurity engineering
* machine learning pipelines
* NLP preprocessing
* REST API development
* browser extension development
* real-time threat detection

and serves as a strong end-to-end cybersecurity portfolio project.
