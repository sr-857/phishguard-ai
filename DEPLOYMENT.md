# Deployment Guide - PhishGuard AI

This guide covers deploying PhishGuard AI to various platforms for live access.

## 🚀 Quick Deploy Options

### Option 1: Vercel (Frontend) + Railway (Backend) - Recommended

#### Frontend Deployment (Vercel)

1. **Prepare Frontend for Deployment**
```bash
cd frontend
npm run build
```

2. **Deploy to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Import your GitHub repository
   - Select the `frontend` directory as root
   - Set build command: `npm run build`
   - Set output directory: `dist`
   - Deploy!

3. **Environment Variables**
   - Add `VITE_API_URL` pointing to your backend URL

#### Backend Deployment (Railway)

1. **Create `Procfile`** (already included)
```
web: uvicorn src.api:app --host 0.0.0.0 --port $PORT
```

2. **Deploy to Railway**
   - Go to [railway.app](https://railway.app)
   - Create new project from GitHub repo
   - Railway will auto-detect Python and deploy
   - Your API will be live!

3. **Update Frontend**
   - Update `VITE_API_URL` in Vercel to point to Railway backend

---

### Option 2: Render (Full Stack)

## ☁️ Option 2: Deploy to Render (Free Forever)

**Pros:** Free forever, no credit card required.
**Cons:** Spins down after 15 mins of inactivity (30s cold start).

### Method A: Using Blueprint (Recommended)
1. Push the `render.yaml` file I just created to GitHub.
2. Go to [Render Dashboard](https://dashboard.render.com/).
3. Click **New +** -> **Blueprint**.
4. Connect your GitHub repository.
5. Click **Apply**.

### Method B: Manual Setup
1. Go to [Render Dashboard](https://dashboard.render.com/).
2. Click **New +** -> **Web Service**.
3. Connect your repository `sr-857/phishguard-ai`.
4. Configure:
   - **Name**: `phishguard-api`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn src.api:app --host 0.0.0.0 --port $PORT`
5. Click **Create Web Service**.

### 🔗 Post-Deployment
1. Copy your new Render URL (e.g., `https://phishguard-api.onrender.com`).
2. Update your GitHub Actions workflow:
   - Edit `.github/workflows/deploy.yml`
   - Update `VITE_API_URL` with the new Render URL.
3. Push changes to redeploy frontend.
   - Create new Static Site
   - Build command: `cd frontend && npm install && npm run build`
   - Publish directory: `frontend/dist`

---

### Option 3: Docker Deployment

1. **Create Dockerfile** (backend)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
```

2. **Create Dockerfile** (frontend)
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build
FROM nginx:alpine
COPY --from=0 /app/dist /usr/share/nginx/html
```

3. **Deploy to any cloud provider** (AWS, GCP, Azure, DigitalOcean)

---

## 🔧 Configuration

### Environment Variables

**Backend:**
- `PORT` - Server port (default: 8000)
- `CORS_ORIGINS` - Allowed origins (set to your frontend URL)

**Frontend:**
- `VITE_API_URL` - Backend API URL

### CORS Configuration

Update `src/api.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-url.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 📝 Post-Deployment Checklist

- [ ] Test API endpoints
- [ ] Verify frontend-backend connection
- [ ] Test email classification
- [ ] Check system status indicator
- [ ] Verify all UI elements load correctly
- [ ] Test on mobile devices
- [ ] Update README with live demo link

---

## 🌐 Custom Domain (Optional)

### Vercel
1. Go to project settings
2. Add custom domain
3. Update DNS records

### Railway
1. Go to project settings
2. Add custom domain
3. Update DNS records

---

## 🔒 Security Recommendations

1. **Rate Limiting**: Add rate limiting to API endpoints
2. **API Keys**: Implement API key authentication for production
3. **HTTPS**: Ensure all traffic uses HTTPS
4. **Environment Variables**: Never commit sensitive data
5. **CORS**: Restrict to specific origins in production

---

## 📊 Monitoring

- Use Vercel Analytics for frontend
- Use Railway metrics for backend
- Consider adding Sentry for error tracking
- Monitor API response times

---

## 💡 Tips

- **Free Tiers**: Both Vercel and Railway offer generous free tiers
- **Build Time**: First deployment may take 5-10 minutes
- **Updates**: Push to GitHub to auto-deploy
- **Logs**: Check deployment logs if issues occur

---

## 🆘 Troubleshooting

**Frontend can't connect to backend:**
- Check CORS settings
- Verify API URL in environment variables
- Check backend is running

**Model not loading:**
- Ensure models are included in deployment
- Check file paths are correct
- Verify NLTK data is downloaded

**Build fails:**
- Check Node.js version (use 18+)
- Check Python version (use 3.8+)
- Review build logs for errors

---

## 📞 Support

If you encounter issues:
1. Check deployment logs
2. Review this guide
3. Open an issue on GitHub
4. Contact: subhajitroy857@gmail.com

---

**Ready to deploy? Choose your platform and follow the steps above!** 🚀
