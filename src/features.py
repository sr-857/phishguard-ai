from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd

def extract_features(df, test_size=0.2, random_state=42, max_features=5000):
    """
    Splits data into train/test sets and extracts TF-IDF features.
    
    Args:
        df (pd.DataFrame): Dataframe with 'cleaned_text' and 'label_num'.
        test_size (float): Proportion of dataset to include in the test split.
        random_state (int): Random seed.
        max_features (int): Max number of features for TF-IDF.
        
    Returns:
        X_train_tfidf, X_test_tfidf, y_train, y_test, vectorizer
    """
    print("Splitting data into train and test sets...")
    X = df['cleaned_text']
    y = df['label_num']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    print("Vectorizing data using TF-IDF...")
    vectorizer = TfidfVectorizer(max_features=max_features)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    
    print(f"Feature extraction complete. Train shape: {X_train_tfidf.shape}, Test shape: {X_test_tfidf.shape}")
    
    return X_train_tfidf, X_test_tfidf, y_train, y_test, vectorizer

if __name__ == "__main__":
    from data_loader import get_processed_data
    df = get_processed_data()
    X_train, X_test, y_train, y_test, vec = extract_features(df)
    print("Features extracted successfully.")
