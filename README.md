# AI-Powered Phishing Email Classifier

## Project Overview
This project implements a machine learning system to classify emails as Legitimate (Ham) or Phishing/Spam. It uses the SMS Spam Collection dataset and compares three algorithms: Naive Bayes, Logistic Regression, and Random Forest.

## Project Structure
- `data/`: Contains the dataset.
- `src/`: Source code.
    - `data_loader.py`: Downloads and cleans data.
    - `features.py`: Implements TF-IDF vectorization.
    - `model_trainer.py`: Trains and tunes models.
    - `evaluation.py`: Evaluates models and generates plots.
    - `inference.py`: Predicts labels for new text.
- `models/`: Saved trained models and vectorizer.
- `results/`: Evaluation metrics and confusion matrix plots.
- `notebooks/`: Jupyter Notebook for demonstration.

## Setup & Usage

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the System (React + FastAPI)**:
    Launch the full industry-level application:
    ```bash
    ./run_system.sh
    ```
    This will start:
    - **Frontend**: http://localhost:5173 (React + Vite)
    - **Backend**: http://localhost:8000 (FastAPI)

3.  **Legacy Streamlit App**:
    If you prefer the simpler prototype:
    ```bash
    ./run_app.sh
    ```

4.  **Run the Full Pipeline (CLI)**:
    You can run the scripts individually or use the provided notebook.
    ```bash
    # 1. Load data, train models, and evaluate
    python3 src/model_trainer.py
    python3 src/evaluation.py
    
    # 2. Run inference example
    python3 src/inference.py
    ```

4.  **Jupyter Notebook**:
    Open `notebooks/Phishing_Email_Classifier.ipynb` to see the step-by-step workflow and analysis.

## Results Summary
The models were evaluated on an unseen test set (20% split).

| Model | Recall | F1-Score | Accuracy |
|-------|--------|----------|----------|
| **Logistic Regression** | **~91.3%** | **~93.5%** | **~98.3%** |
| Naive Bayes | ~87.3% | ~92.5% | ~98.1% |
| Random Forest | ~86.6% | ~92.5% | ~98.1% |

**Logistic Regression** was selected as the best model due to its superior Recall score, which is critical for detecting phishing attempts (minimizing False Negatives).

## Technical Details
- **Text Cleaning**: Lowercasing, regex for HTML/URLs, stopword removal, Porter Stemming.
- **Vectorization**: TF-IDF (top 5000 features).
- **Hyperparameter Tuning**: GridSearchCV with 5-fold cross-validation, optimizing for Recall.
