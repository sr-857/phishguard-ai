import joblib
import os
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Re-use cleaning logic or import it (importing is better to avoid duplication)
# However, for a standalone inference script, we might want it self-contained or import from data_loader
from data_loader import clean_text

# Define paths relative to this script to ensure they work from anywhere
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")

def load_resources(model_name='Logistic_Regression'):
    """Loads the vectorizer and the specified model."""
    vectorizer_path = os.path.join(MODELS_DIR, "tfidf_vectorizer.pkl")
    model_path = os.path.join(MODELS_DIR, f"{model_name}.pkl")
    
    if not os.path.exists(vectorizer_path) or not os.path.exists(model_path):
        raise FileNotFoundError("Model or vectorizer not found. Please train the models first.")
        
    vectorizer = joblib.load(vectorizer_path)
    model = joblib.load(model_path)
    
    return vectorizer, model

def predict_email(text, vectorizer, model):
    """
    Predicts whether an email is Phishing (Spam) or Ham.
    
    Args:
        text (str): Raw email text.
        vectorizer: Fitted TfidfVectorizer.
        model: Trained classification model.
        
    Returns:
        dict: Prediction result with label and probability.
    """
    cleaned_text = clean_text(text)
    features = vectorizer.transform([cleaned_text])
    
    prediction = model.predict(features)[0]
    proba = model.predict_proba(features)[0]
    
    label = "Phishing/Spam" if prediction == 1 else "Legitimate/Ham"
    score = proba[1] if prediction == 1 else proba[0]
    
    return {
        "label": label,
        "probability": f"{score:.4f}",
        "raw_text": text
    }

if __name__ == "__main__":
    # Example usage
    try:
        vec, model = load_resources()
        
        sample_spam = "URGENT! You have won a 1 week FREE membership in our £100,000 Prize Jackpot! Txt WORD: CLAIM to No: 81010 T&C www.dbuk.net LCCLTD POBOX 4403LDNW1A7RW18"
        sample_ham = "Hey, are we still meeting for lunch tomorrow?"
        
        print("Testing Inference:")
        print(predict_email(sample_spam, vec, model))
        print(predict_email(sample_ham, vec, model))
        
    except FileNotFoundError as e:
        print(e)
