from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import re

# Load trained model and vectorizer
model = joblib.load("model/phishing_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

with open(
    "dataset/trusted_domains.txt",
    "r",
    encoding="utf-8"
) as file:

    trusted_domains = set(
        line.strip().lower()
        for line in file
    )

print(f"Loaded {len(trusted_domains)} trusted domains")

def extract_domains(text):

    # Find domains from email addresses
    domains = re.findall(
        r'@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})',
        text
    )

    # Convert to lowercase
    domains = [domain.lower() for domain in domains]

    return domains

# Create Flask app
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "PhishGuard AI Backend Running"

@app.route('/predict', methods=['POST'])
def predict():

    try:
        # Get JSON data
        data = request.get_json()

        # Extract email text
        email_text = data.get('email', '')

        # Vectorize
        email_vector = vectorizer.transform([email_text])

        # Predict
        # Predict
        prediction = model.predict(email_vector)[0]

        # Probability scores
        probability = model.predict_proba(email_vector)[0]

        confidence = round(max(probability) * 100, 2)

        # Extract domains from email
        domains = extract_domains(email_text)

        # Check trusted domains
        trusted_found = any(
            domain in trusted_domains
            for domain in domains
        )

        # Reduce phishing confidence if trusted domain found
        if trusted_found and prediction == 1:

            confidence = max(confidence - 20, 0)

        # Increase safe confidence slightly
        if trusted_found and prediction == 0:

            confidence = min(confidence + 10, 100)

        # Convert result
        if prediction == 1 and confidence >= 85:
            result = "High Risk Phishing"

        elif prediction == 1 and confidence >= 60:
            result = "Suspicious Email"

        else:
            result = "Likely Safe"

        return jsonify({
            'prediction': result,
            'confidence': confidence
        })

    except Exception as e:
        return jsonify({
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)