import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import joblib
import os

MODELS_DIR = "models"
RESULTS_DIR = "results"

def evaluate_model(model, X_test, y_test, model_name):
    """
    Evaluates a trained model and prints metrics.
    Generates a confusion matrix plot.
    
    Args:
        model: Trained model object.
        X_test: Test features.
        y_test: Test labels.
        model_name: Name of the model.
        
    Returns:
        dict: Dictionary of metrics.
    """
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)
        
    y_pred = model.predict(X_test)
    
    metrics = {
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred),
        'Recall': recall_score(y_test, y_pred),
        'F1-Score': f1_score(y_test, y_pred)
    }
    
    print(f"\n--- {model_name} Evaluation ---")
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")
        
    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Ham', 'Spam'], yticklabels=['Ham', 'Spam'])
    plt.title(f'Confusion Matrix - {model_name}')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, f"confusion_matrix_{model_name}.png"))
    plt.close()
    
    return metrics

if __name__ == "__main__":
    from data_loader import get_processed_data
    from features import extract_features
    
    # Load data and features
    df = get_processed_data()
    X_train, X_test, y_train, y_test, vec = extract_features(df)
    
    # Load models
    model_files = [f for f in os.listdir(MODELS_DIR) if f.endswith('.pkl') and f != 'tfidf_vectorizer.pkl']
    
    results = []
    
    for model_file in model_files:
        model_name = model_file.replace('.pkl', '')
        model_path = os.path.join(MODELS_DIR, model_file)
        model = joblib.load(model_path)
        
        metrics = evaluate_model(model, X_test, y_test, model_name)
        metrics['Model'] = model_name
        results.append(metrics)
        
    # Compare models
    results_df = pd.DataFrame(results)
    print("\n--- Model Comparison ---")
    print(results_df)
    results_df.to_csv(os.path.join(RESULTS_DIR, "model_comparison.csv"), index=False)
