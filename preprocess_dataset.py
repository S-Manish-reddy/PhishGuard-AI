import pandas as pd
import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load dataset
df = pd.read_csv("dataset/Phishing_Email.csv")

print("Original Shape:", df.shape)

# Keep only required columns
df = df[['Email Text', 'Email Type']]

# Remove missing values
df.dropna(inplace=True)

# Remove duplicate emails
df.drop_duplicates(subset=['Email Text'], inplace=True)

# Convert labels
df['label'] = df['Email Type'].map({
    'Safe Email': 0,
    'Phishing Email': 1
})

# Remove failed labels
df.dropna(subset=['label'], inplace=True)

# Stopwords
stop_words = set(stopwords.words('english'))

# Cleaning function
def clean_text(text):

    text = str(text)

    # Lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r'http\\S+', '', text)

    # Remove email addresses
    text = re.sub(r'\\S+@\\S+', '', text)

    # Remove punctuation
    text = re.sub(r'[^a-zA-Z\\s]', ' ', text)

    # Tokenize
    words = word_tokenize(text)

    # Remove stopwords only
    words = [word for word in words if word not in stop_words]

    # Join back
    text = " ".join(words)

    return text

# Apply cleaning
df['cleaned_text'] = df['Email Text'].apply(clean_text)

# Remove empty cleaned rows only
df = df[df['cleaned_text'].str.strip() != '']

# Keep final columns
final_df = df[['cleaned_text', 'label']]

print("Cleaned Shape:", final_df.shape)

print("\nLabel Distribution:")
print(final_df['label'].value_counts())

# Save processed dataset
final_df.to_csv("dataset/processed_dataset.csv", index=False)

print("\nDATASET CLEANING COMPLETE")