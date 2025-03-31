import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re

# NLTLK resources download
print("Downloading NLTK resources...")
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
print("NLTK resources downloaded.")

def preprocess(text):
    """
    Clean and preprocess text:
    - Lowercase
    - Remove special chars
    - Remove stopwords
    - Lemmatization
    """
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special characters
    tokens = word_tokenize(text=text) # Tokenize
    stopwords_set = set(stopwords.words('english'))  # Get stopwords
    tokens = [word for word in tokens if word not in stopwords_set]  # Remove stopwords
    lemmatizer = WordNetLemmatizer()  # Initialize lemmatizer
    tokens = [lemmatizer.lemmatize(word) for word in tokens]  # Lemmatize
    return ' '.join(tokens)  # Join tokens back to string

