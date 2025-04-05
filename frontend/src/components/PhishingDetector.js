

import React, { useState } from "react";
import "./PhishingDetector.css";

export default function PhishingDetector() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const checkUrl = async () => {
    if (!url.trim()) return;

    setLoading(true);
    setResult(null);

    try {
      const response = await fetch("http://localhost:3001/api/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      });

      const data = await response.json();
      setResult(data.prediction);
    } catch (error) {
      console.error("Error fetching prediction:", error);
      setResult("error");
    }

    setLoading(false);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      checkUrl();
    }
  };

  return (
    <div className="detector-container">
      <div className="detector-card">
        <div className="header">
          <div className="logo">
            <i className="shield-icon"></i>
          </div>
          <h1>PhishNet AI</h1>
          <p className="subtitle">Verify website safety before you visit</p>
        </div>
        
        <div className="input-section">
          <div className="input-wrapper">
            <i className="url-icon"></i>
            <input
              type="text"
              placeholder="Enter a URL to check..."
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              onKeyPress={handleKeyPress}
              className="url-input"
            />
            {url && (
              <button 
                className="clear-btn" 
                onClick={() => setUrl("")}
                aria-label="Clear input"
              >
                ×
              </button>
            )}
          </div>
          <button 
            onClick={checkUrl} 
            className="check-btn"
            disabled={loading || !url.trim()}
          >
            {loading ? (
              <span className="loading-spinner"></span>
            ) : (
              <>Check Security</>
            )}
          </button>
        </div>

        {result && (
          <div className={`result-container ${result === "bad" ? "danger" : "safe"}`}>
            <div className="result-icon">
              {result === "bad" ? "⚠️" : "✅"}
            </div>
            <div className="result-details">
              <h3>{result === "bad" ? "Potential Threat Detected" : "Safe to Visit"}</h3>
              <p>
                {result === "bad" 
                  ? "This URL shows signs of being a phishing attempt. Exercise caution." 
                  : "No phishing indicators found in this URL."
                }
              </p>
            </div>
          </div>
        )}
        
        <div className="footer">
          <p>Powered by ML-based phishing detection</p>
        </div>
      </div>
    </div>
  );

}