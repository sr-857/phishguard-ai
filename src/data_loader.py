import os
import urllib.request
import zipfile
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Ensure NLTK data is downloaded
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

DATA_URL = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"
DATA_DIR = "data"
ZIP_PATH = os.path.join(DATA_DIR, "smsspamcollection.zip")
EXTRACT_PATH = os.path.join(DATA_DIR, "extracted")
FILE_PATH = os.path.join(EXTRACT_PATH, "SMSSpamCollection")

def download_data():
    """Downloads and extracts the SMS Spam Collection dataset."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    if not os.path.exists(ZIP_PATH):
        print(f"Downloading dataset from {DATA_URL}...")
        urllib.request.urlretrieve(DATA_URL, ZIP_PATH)
        print("Download complete.")
    
    if not os.path.exists(EXTRACT_PATH):
        print("Extracting dataset...")
        with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
            zip_ref.extractall(EXTRACT_PATH)
        print("Extraction complete.")

def load_data():
    """Loads the dataset into a pandas DataFrame."""
    download_data()
    # The dataset is tab-separated
    df = pd.read_csv(FILE_PATH, sep='\t', header=None, names=['label', 'text'])
    return df

def clean_text(text):
    """
    Cleans the email text:
    1. Lowercase
    2. Remove HTML tags (basic regex)
    3. Remove URLs
    4. Remove special characters
    5. Remove stopwords
    6. Stemming
    """
    # 1. Lowercase
    text = text.lower()
    
    # 2. Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    
    # 3. Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # 4. Remove special characters and numbers (keep only letters)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Tokenize (split by whitespace)
    words = text.split()
    
    # 5. Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if w not in stop_words]
    
    # 6. Stemming
    stemmer = PorterStemmer()
    words = [stemmer.stem(w) for w in words]
    
    return " ".join(words)

def get_processed_data():
    """Loads and preprocesses the data."""
    df = load_data()
    print("Cleaning data...")
    df['cleaned_text'] = df['text'].apply(clean_text)
    
    # Encode labels: ham -> 0, spam -> 1
    df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})
    
    print("Data processing complete.")
    return df

if __name__ == "__main__":
    df = get_processed_data()
    print(df.head())
    print(df['label'].value_counts())
