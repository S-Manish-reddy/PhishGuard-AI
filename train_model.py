import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load processed dataset
df = pd.read_csv("dataset/processed_dataset.csv")

# Features and labels
X = df['cleaned_text']
y = df['label']

# Convert text into TF-IDF vectors
vectorizer = TfidfVectorizer(
    max_features=8000,
    ngram_range=(1,2),
    sublinear_tf=True
)
X_vectorized = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = MultinomialNB()

# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"\nMODEL ACCURACY: {accuracy * 100:.2f}%")

# Detailed report
print("\nCLASSIFICATION REPORT:\n")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "model/phishing_model.pkl")

# Save vectorizer
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("\nMODEL AND VECTORIZER SAVED SUCCESSFULLY")