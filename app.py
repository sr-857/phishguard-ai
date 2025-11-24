import streamlit as st
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Add src to path
sys.path.append(os.path.abspath('src'))

try:
    from inference import predict_email, load_resources
except ImportError:
    sys.path.append(os.path.join(os.getcwd(), 'src'))
    from inference import predict_email, load_resources

# Page Config
st.set_page_config(
    page_title="Sentinel AI | Phishing Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load Resources
@st.cache_resource
def get_model():
    try:
        return load_resources('Logistic_Regression')
    except Exception:
        return None, None

vectorizer, model = get_model()

# Session State
if 'history' not in st.session_state:
    st.session_state.history = []

# --- CUSTOM CSS & ASSETS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    /* Global Reset & Typography */
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
        background-color: #050505;
        color: #e0e0e0;
    }
    
    /* Gradient Background for Main App */
    .stApp {
        background: radial-gradient(circle at 50% 10%, #1a1a2e 0%, #000000 100%);
    }

    /* Hero Section Typography */
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        animation: fadeInDown 1s ease-out;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        color: #a0a0a0;
        text-align: center;
        margin-bottom: 3rem;
        font-weight: 300;
        animation: fadeInUp 1s ease-out 0.5s backwards;
    }

    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(0, 100, 255, 0.1);
        border-color: rgba(79, 172, 254, 0.3);
    }

    /* Input Area Styling */
    .stTextArea textarea {
        background-color: rgba(0, 0, 0, 0.3) !important;
        border: 1px solid #333 !important;
        border-radius: 12px !important;
        color: #fff !important;
        font-size: 1rem !important;
        padding: 1rem !important;
        transition: border-color 0.3s ease;
    }
    
    .stTextArea textarea:focus {
        border-color: #4facfe !important;
        box-shadow: 0 0 15px rgba(79, 172, 254, 0.2) !important;
    }

    /* Custom Button */
    .stButton > button {
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        color: #000;
        font-weight: 700;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(79, 172, 254, 0.4);
    }
    
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(79, 172, 254, 0.6);
        color: #000;
    }

    /* Result Badges */
    .result-badge {
        padding: 1.5rem;
        border-radius: 16px;
        text-align: center;
        animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    
    .phishing-badge {
        background: rgba(255, 68, 68, 0.1);
        border: 1px solid #ff4444;
        color: #ff4444;
        box-shadow: 0 0 30px rgba(255, 68, 68, 0.2);
    }
    
    .safe-badge {
        background: rgba(0, 204, 0, 0.1);
        border: 1px solid #00cc00;
        color: #00cc00;
        box-shadow: 0 0 30px rgba(0, 204, 0, 0.2);
    }

    /* Animations */
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes popIn {
        from { opacity: 0; transform: scale(0.8); }
        to { opacity: 1; transform: scale(1); }
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    </style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown('<div class="hero-title">SENTINEL AI</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Next-Generation Phishing Detection System</div>', unsafe_allow_html=True)

# --- MAIN LAYOUT ---
col_main, col_side = st.columns([2, 1], gap="large")

with col_main:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 📨 Analyze Email Content")
    email_text = st.text_area("Email Content", height=250, placeholder="Paste the suspicious email header and body here for instant analysis...", label_visibility="collapsed")
    
    if st.button("🛡️ SCAN FOR THREATS"):
        if not email_text.strip():
            st.warning("⚠️ Please enter content to analyze.")
        elif not model:
            st.error("❌ Model not loaded. System offline.")
        else:
            with st.spinner("🔄 Decrypting patterns & analyzing heuristics..."):
                # Inference
                result = predict_email(email_text, vectorizer, model)
                label = result['label']
                prob = float(result['probability'])
                is_phishing = "Phishing" in label
                
                # Update History
                st.session_state.history.insert(0, {
                    "time": datetime.now().strftime("%H:%M"),
                    "label": "PHISHING" if is_phishing else "SAFE",
                    "conf": prob,
                    "snippet": email_text[:40] + "..."
                })
                
                # Display Result
                st.markdown("---")
                if is_phishing:
                    st.markdown(f"""
                        <div class="result-badge phishing-badge">
                            <h1 style="margin:0; font-size: 2.5rem;">🚫 THREAT DETECTED</h1>
                            <p style="margin:10px 0 0 0; opacity:0.8;">CONFIDENCE: {prob*100:.2f}%</p>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                        <div class="result-badge safe-badge">
                            <h1 style="margin:0; font-size: 2.5rem;">✅ SAFE TO PROCEED</h1>
                            <p style="margin:10px 0 0 0; opacity:0.8;">CONFIDENCE: {prob*100:.2f}%</p>
                        </div>
                    """, unsafe_allow_html=True)
                
                # Technical Details
                with st.expander("🔍 View Forensic Analysis"):
                    st.json(result)
                    
    st.markdown('</div>', unsafe_allow_html=True)

with col_side:
    # Live Feed
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 📡 Live Threat Feed")
    
    if st.session_state.history:
        for item in st.session_state.history[:4]:
            color = "#ff4444" if item['label'] == "PHISHING" else "#00cc00"
            st.markdown(f"""
                <div style="border-bottom: 1px solid rgba(255,255,255,0.1); padding: 10px 0;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-weight:bold; color:{color};">{item['label']}</span>
                        <span style="font-size:0.8rem; opacity:0.6;">{item['time']}</span>
                    </div>
                    <div style="font-size:0.85rem; opacity:0.7; margin-top:4px;">{item['snippet']}</div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("System Ready. Waiting for input...")
        
    if st.button("Clear Feed", type="secondary"):
        st.session_state.history = []
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # System Status
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 🖥️ System Status")
    st.markdown("""
        <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
            <span>Engine</span>
            <span style="color:#4facfe;">Online</span>
        </div>
        <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
            <span>Model</span>
            <span style="color:#4facfe;">Logistic Regression v1.0</span>
        </div>
        <div style="display:flex; justify-content:space-between;">
            <span>Accuracy</span>
            <span style="color:#00f2fe;">98.3%</span>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
