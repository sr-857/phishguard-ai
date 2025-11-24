from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import joblib
import os

MODELS_DIR = "models"

def train_models(X_train, y_train):
    """
    Trains and tunes Naive Bayes, Logistic Regression, and Random Forest models.
    
    Args:
        X_train: Training features.
        y_train: Training labels.
        
    Returns:
        dict: Dictionary of trained best models.
    """
    if not os.path.exists(MODELS_DIR):
        os.makedirs(MODELS_DIR)
        
    models = {
        'Naive_Bayes': {
            'model': MultinomialNB(),
            'params': {
                'alpha': [0.1, 0.5, 1.0]
            }
        },
        'Logistic_Regression': {
            'model': LogisticRegression(class_weight='balanced', max_iter=1000),
            'params': {
                'C': [0.1, 1, 10],
                'solver': ['liblinear', 'lbfgs']
            }
        },
        'Random_Forest': {
            'model': RandomForestClassifier(class_weight='balanced', random_state=42),
            'params': {
                'n_estimators': [50, 100, 200],
                'max_depth': [None, 10, 20],
                'min_samples_split': [2, 5]
            }
        }
    }
    
    trained_models = {}
    
    for name, config in models.items():
        print(f"Training {name}...")
        grid = GridSearchCV(config['model'], config['params'], cv=5, scoring='recall', n_jobs=-1)
        grid.fit(X_train, y_train)
        
        best_model = grid.best_estimator_
        trained_models[name] = best_model
        
        print(f"Best params for {name}: {grid.best_params_}")
        print(f"Best Recall score (CV): {grid.best_score_:.4f}")
        
        # Save model
        joblib.dump(best_model, os.path.join(MODELS_DIR, f"{name}.pkl"))
        
    return trained_models

if __name__ == "__main__":
    from data_loader import get_processed_data
    from features import extract_features
    
    df = get_processed_data()
    X_train, X_test, y_train, y_test, vec = extract_features(df)
    
    # Save vectorizer
    if not os.path.exists(MODELS_DIR):
        os.makedirs(MODELS_DIR)
    joblib.dump(vec, os.path.join(MODELS_DIR, "tfidf_vectorizer.pkl"))
    
    train_models(X_train, y_train)
