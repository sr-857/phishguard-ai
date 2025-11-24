from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import sys
import os
import uvicorn
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add src to path to import inference module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from inference import predict_email, load_resources

# Initialize Rate Limiter
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="PhishGuard AI API", version="1.0")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS Middleware - Production Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://sr-857.github.io",  # GitHub Pages
        "http://localhost:5173",      # Local development
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST"],   # Restrict methods
    allow_headers=["*"],
)

# Load Model at Startup
try:
    vectorizer, model = load_resources('Logistic_Regression')
    logger.info("Model loaded successfully.")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    vectorizer = None
    model = None

class EmailRequest(BaseModel):
    text: str = Field(..., max_length=10000, description="Email content to analyze")

@app.get("/")
@limiter.limit("10/minute")
def read_root(request: Request):
    return {"status": "online", "model": "Logistic Regression"}

@app.post("/predict")
@limiter.limit("20/minute")
def predict(request: Request, email_request: EmailRequest):
    if not vectorizer or not model:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        result = predict_email(email_request.text, vectorizer, model)
        return result
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
