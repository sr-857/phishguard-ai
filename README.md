<div align="center">

![PhishGuard AI Logo](.github/logo.png)

# 🛡️ PhishGuard AI
### Next-Gen AI Phishing Detection System

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-18-61DAFB.svg?style=flat-square&logo=react&logoColor=black)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

### 🚀 **[Launch Live Demo](https://sr-857.github.io/phishguard-ai/)** 🚀

[Features](#-features) •
[Architecture](#-architecture) •
[Installation](#-installation) •
[API](#-api-documentation) •
[Contributing](#-contributing)

</div>

---

## 💡 The Problem
Phishing attacks account for **90% of all data breaches**, with AI-generated scams becoming increasingly difficult to detect. Traditional rule-based filters struggle to keep up with these sophisticated threats.

## 🛡️ The Solution
**PhishGuard AI** is an intelligent defense layer that leverages Machine Learning (Logistic Regression) and Natural Language Processing (NLP) to analyze email intent, context, and linguistic patterns in real-time.

> **"Don't just block. Understand."**

---

## ✨ Key Features

### 🧠 Intelligent Detection
- **98.3% Accuracy**: Trained on the SMS Spam Collection dataset.
- **High Recall (91.3%)**: Prioritizes catching threats to minimize missed attacks.
- **Real-Time Analysis**: Sub-100ms inference time.

### 🎨 Next-Gen UI/UX
- **Cyberpunk Aesthetic**: Glassmorphism, neon accents, and Digital Rain effects.
- **Live Threat Feed**: Real-time visualization of scanned emails.
- **Forensic Breakdown**: Detailed confidence scores and probability analysis.

---

## 🎬 Demo

### Dashboard Interface

![PhishGuard AI Dashboard](.github/dashboard-demo.png)

### Key Capabilities

1. **Email Analysis**: Paste suspicious email content for instant classification
2. **Threat Visualization**: Color-coded results (Red = Phishing, Green = Safe)
3. **Forensic Details**: Expandable technical analysis with raw model output
4. **Scan History**: Chronological feed of all analyzed emails
5. **System Status**: Real-time engine health monitoring

### 🎥 Live Demo

Watch PhishGuard AI in action:

![Live Demo Recording](.github/dashboard_demo_1763963867984.webp)

**Try it yourself:**
1. Clone the repository
2. Run `./run_system.sh`
3. Open http://localhost:5173
4. Paste a suspicious email and click "SCAN FOR THREATS"

---

## 🛠️ Tech Stack

### Frontend
- **Framework**: React 18 with Vite
- **Styling**: Vanilla CSS with custom animations
- **Fonts**: Google Fonts (Outfit, Orbitron)
- **Effects**: Glassmorphism, Digital Rain, Custom Cursors

### Backend
- **Framework**: FastAPI
- **Server**: Uvicorn (ASGI)
- **CORS**: Enabled for cross-origin requests

### Machine Learning
- **Algorithm**: Logistic Regression
- **Feature Engineering**: TF-IDF Vectorization
- **Text Processing**: NLTK (stopwords, stemming)
- **Model Persistence**: Joblib
- **Evaluation**: scikit-learn metrics

### Data
- **Dataset**: SMS Spam Collection (UCI ML Repository)
- **Size**: 5,574 messages
- **Split**: 80% training, 20% testing

---

## 📦 Installation

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn
- Git

### Clone Repository

```bash
git clone https://github.com/sr-857/phishguard-ai.git
cd phishguard-ai
```

### Backend Setup

```bash
# Install Python dependencies
pip install -r requirements.txt

# Download NLTK data (automatic on first run)
python -c "import nltk; nltk.download('stopwords')"

# Train models (if not already trained)
python src/model_trainer.py
```

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Return to root
cd ..
```

---

## 🚀 Usage

### Quick Start (Recommended)

```bash
# Launch both frontend and backend with one command
./run_system.sh
```

This will start:
- **Backend API**: http://localhost:8000
- **Frontend Dashboard**: http://localhost:5173

### Manual Start

#### Backend Only
```bash
uvicorn src.api:app --reload --port 8000
```

#### Frontend Only
```bash
cd frontend
npm run dev
```

---

## 🏗️ Architecture

```mermaid
graph TD
    User[👤 User] -->|Access Dashboard| Frontend[⚛️ React Frontend\n(GitHub Pages)]
    Frontend -->|POST /predict| Backend[🚀 FastAPI Backend\n(Railway)]
    
    subgraph "Backend Services"
        Backend -->|Text Processing| NLP[📝 NLTK Preprocessing]
        NLP -->|Vectorization| TFIDF[🧮 TF-IDF Vectorizer]
        TFIDF -->|Inference| Model[🤖 Logistic Regression Model]
    end
    
    Model -->|Prediction & Score| Backend
    Backend -->|JSON Response| Frontend
    Frontend -->|Visual Feedback| User
    
    style Frontend fill:#61DAFB,stroke:#333,stroke-width:2px,color:black
    style Backend fill:#009688,stroke:#333,stroke-width:2px,color:white
    style Model fill:#FF9800,stroke:#333,stroke-width:2px,color:black
```

### Data Flow
1. **Input**: User pastes email content into the React dashboard.
2. **Request**: Frontend sends a secure API request to the FastAPI backend.
3. **Processing**: Backend cleans text (stopwords, stemming) and vectorizes it.
4. **Inference**: ML model predicts probability of phishing.
5. **Response**: Result is returned and visualized with confidence scores.

---

### Testing the System

1. Open http://localhost:5173 in your browser
2. Paste a suspicious email in the text area
3. Click "🛡️ SCAN FOR THREATS"
4. View results and confidence score
5. Check the Live Threat Feed for history

### Example Phishing Email

```
URGENT! You have won a £100,000 Prize Jackpot! 
Click here to claim: http://suspicious-link.com
Reply with your bank details to: scammer@fake.com
```

---

## 📚 API Documentation

### Base URL
```
http://localhost:8000
```

### Endpoints

#### Health Check
```http
GET /
```

**Response**
```json
{
  "status": "online",
  "model": "Logistic Regression"
}
```

#### Predict Email
```http
POST /predict
Content-Type: application/json
```

**Request Body**
```json
{
  "text": "Your email content here"
}
```

**Response**
```json
{
  "label": "Phishing/Spam",
  "probability": "0.9234",
  "raw_text": "Your email content here"
}
```

### Interactive API Docs

Visit http://localhost:8000/docs for Swagger UI documentation.

---

## 📊 Model Performance

### Metrics (Logistic Regression)

| Metric | Score |
|--------|-------|
| **Accuracy** | 98.3% |
| **Precision** | 98.5% |
| **Recall** | 91.3% |
| **F1-Score** | 94.8% |

### Why Logistic Regression?

We chose Logistic Regression over Naive Bayes and Random Forest because:

1. **High Recall**: 91.3% recall minimizes false negatives (missed phishing emails)
2. **Fast Inference**: Real-time predictions with minimal latency
3. **Interpretability**: Clear feature importance for transparency
4. **Efficiency**: Low memory footprint and quick training

---

## 📁 Project Structure

```
phishguard-ai/
├── .github/                    # GitHub assets
│   ├── logo.png               # Repository logo
│   └── dashboard-demo.png     # Demo screenshot
├── frontend/                   # React application
│   ├── public/
│   │   └── cyber_background.png
│   ├── src/
│   │   ├── components/
│   │   │   ├── DigitalRain.jsx
│   │   │   └── Testimonials.jsx
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── src/                        # Backend & ML
│   ├── api.py                 # FastAPI server
│   ├── data_loader.py         # Dataset handling
│   ├── features.py            # Feature engineering
│   ├── model_trainer.py       # Model training
│   ├── evaluation.py          # Performance metrics
│   └── inference.py           # Prediction engine
├── models/                     # Trained models
│   ├── Logistic_Regression.pkl
│   ├── tfidf_vectorizer.pkl
│   └── ...
├── .gitignore
├── requirements.txt
├── run_system.sh              # Launch script
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
└── README.md
```

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Start

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Contact

**Developer**: Subhajit Roy

- 📧 Email: subhajitroy857@gmail.com
- 💼 LinkedIn: [linkedin.com/in/sr857](https://linkedin.com/in/sr857)
- 🐙 GitHub: [github.com/sr-857](https://github.com/sr-857)

---

## 🙏 Acknowledgments

- **Dataset**: [SMS Spam Collection](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection) from UCI ML Repository
- **Inspiration**: Modern cybersecurity dashboards and threat intelligence platforms
- **Libraries**: React, FastAPI, scikit-learn, NLTK, and the amazing open-source community

---

<div align="center">

### ⭐ Star this repository if you found it helpful!

Made with ❤️ and ☕ by [Subhajit Roy](https://github.com/sr-857)

</div>
