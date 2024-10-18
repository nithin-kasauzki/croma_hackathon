import re
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower()

def tokenize_text(text):
    cleaned_text = clean_text(text)
    tokens = word_tokenize(cleaned_text)
    return tokens

if __name__ == "__main__":
    text = "Example text to preprocess!"
    cleaned = clean_text(text)
    tokens = tokenize_text(cleaned)
    print(f"Cleaned Text: {cleaned}")
    print(f"Tokens: {tokens}")