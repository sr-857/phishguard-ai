from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sys
import os
import uvicorn

# Add src to path to import inference module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from inference import predict_email, load_resources

app = FastAPI(title="Phishing Classifier API", version="1.0")

# CORS Middleware to allow requests from React Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Model at Startup
try:
    vectorizer, model = load_resources('Logistic_Regression')
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    vectorizer = None
    model = None

class EmailRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"status": "online", "model": "Logistic Regression"}

@app.post("/predict")
def predict(request: EmailRequest):
    if not vectorizer or not model:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        result = predict_email(request.text, vectorizer, model)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
