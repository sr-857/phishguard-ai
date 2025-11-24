import { useState, useEffect } from 'react'
import './App.css'
import DigitalRain from './components/DigitalRain'
import Testimonials from './components/Testimonials'

function App() {
  const [emailText, setEmailText] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [history, setHistory] = useState([])
  const [systemStatus, setSystemStatus] = useState('Checking...')

  const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

  useEffect(() => {
    const checkHealth = async () => {
      try {
        const response = await fetch(`${API_URL}/`)
        if (response.ok) {
          setSystemStatus('Online')
        } else {
          setSystemStatus('Offline')
        }
      } catch (e) {
        setSystemStatus('Offline')
      }
    }

    checkHealth()
    const interval = setInterval(checkHealth, 30000) // Check every 30s
    return () => clearInterval(interval)
  }, [])

  const analyzeEmail = async () => {
    if (!emailText.trim()) return

    setLoading(true)
    setResult(null)

    try {
      const response = await fetch(`${API_URL}/predict`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: emailText }),
      })

      const data = await response.json()
      setResult(data)

      // Add to history
      const isPhishing = data.label.includes('Phishing')
      const newEntry = {
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        label: isPhishing ? 'PHISHING' : 'SAFE',
        snippet: emailText.substring(0, 40) + '...',
        conf: parseFloat(data.probability)
      }
      setHistory(prev => [newEntry, ...prev])

    } catch (error) {
      console.error('Error:', error)
      alert('Failed to connect to the analysis engine. Is the backend running?')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app-container">
      <div className="background-container">
        <div className="background-image"></div>
        <DigitalRain />
        <div className="scanlines"></div>
      </div>

      <div className="hero-section">
        <h1 className="hero-title">PHISHGUARD AI</h1>
        <p className="hero-subtitle">Next-Generation Phishing Detection System</p>
      </div>

      <div className="main-layout">
        <div className="glass-card main-card">
          <h3>📨 Analyze Email Content</h3>
          <textarea
            className="email-input"
            placeholder="Paste the suspicious email header and body here for instant analysis..."
            value={emailText}
            onChange={(e) => setEmailText(e.target.value)}
          />

          <button
            className="analyze-btn"
            onClick={analyzeEmail}
            disabled={loading}
          >
            {loading ? '🔄 ANALYZING...' : '🛡️ SCAN FOR THREATS'}
          </button>

          {result && (
            <div className={`result-badge ${result.label.includes('Phishing') ? 'phishing' : 'safe'}`}>
              <h1>{result.label.includes('Phishing') ? '🚫 THREAT DETECTED' : '✅ SAFE TO PROCEED'}</h1>
              <p>CONFIDENCE: {(parseFloat(result.probability) * 100).toFixed(2)}%</p>

              <div className="technical-details">
                <details>
                  <summary>View Forensic Analysis</summary>
                  <pre>{JSON.stringify(result, null, 2)}</pre>
                </details>
              </div>
            </div>
          )}
        </div>

        <div className="sidebar">
          <div className="glass-card">
            <h3>📡 Live Threat Feed</h3>
            {history.length === 0 ? (
              <p className="empty-feed">System Ready. Waiting for input...</p>
            ) : (
              <div className="feed-list">
                {history.map((item, index) => (
                  <div key={index} className="feed-item">
                    <div className="feed-header">
                      <span className={`feed-label ${item.label.toLowerCase()}`}>{item.label}</span>
                      <span className="feed-time">{item.time}</span>
                    </div>
                    <div className="feed-snippet">{item.snippet}</div>
                  </div>
                ))}
              </div>
            )}
            {history.length > 0 && (
              <button className="clear-btn" onClick={() => setHistory([])}>Clear Feed</button>
            )}
          </div>

          <div className="glass-card status-card">
            <h3>🖥️ System Status</h3>
            <div className="status-row">
              <span>Engine</span>
              <span className={systemStatus === 'Online' ? 'status-online' : 'status-offline'}>{systemStatus}</span>
            </div>
            <div className="status-row">
              <span>Model</span>
              <span className="status-online">Logistic Regression v1.0</span>
            </div>
            <div className="status-row">
              <span>Accuracy</span>
              <span className="status-value">98.3%</span>
            </div>
          </div>
        </div>
      </div>

      <Testimonials />

      <footer className="app-footer">
        <div className="glass-card footer-content">
          <h3>👨‍💻 Developer Contact</h3>
          <div className="contact-links">
            <a href="mailto:subhajitroy857@gmail.com" className="contact-item">
              <svg className="icon" viewBox="0 0 24 24" fill="currentColor">
                <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" />
              </svg>
              subhajitroy857@gmail.com
            </a>
            <a href="https://linkedin.com/in/sr857" target="_blank" rel="noopener noreferrer" className="contact-item">
              <svg className="icon" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.32 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.79M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z" />
              </svg>
              linkedin.com/in/sr857
            </a>
            <a href="https://github.com/sr-857" target="_blank" rel="noopener noreferrer" className="contact-item">
              <svg className="icon" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2A10 10 0 0 0 2 12c0 4.42 2.87 8.17 7.12 9.59.5.09.68-.22.68-.48v-1.69c-2.79.6-3.38-1.34-3.38-1.34-.46-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.89 1.52 2.34 1.08 2.91.83.09-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.92 0-1.11.38-1.55 1.02-2.53-.1-.28-.45-1.2.1-2.5 0 0 .84-.27 2.75 1.02a9.58 9.58 0 0 1 5 0c1.91-1.29 2.75-1.02 2.75-1.02.55 1.3.2 2.22.1 2.5.63.98 1.02 1.42 1.02 2.53 0 3.84-2.33 4.66-4.56 4.91.36.31.69.92.69 1.85V21c0 .27.18.57.69.48A10 10 0 0 0 22 12c0-5.52-4.48-10-10-10z" />
              </svg>
              github.com/sr-857
            </a>
          </div>
        </div>
      </footer>
    </div>
  )
}

export default App
