# PhisNet AI

PhisNet AI is an advanced phishing detection system that analyzes URLs to determine whether they are phishing or legitimate using machine learning.

## Features
- *Phishing Detection*: Uses machine learning to classify URLs as phishing or legitimate.
- *User-Friendly Interface*: Simple and intuitive frontend for users to input URLs.
- *Real-time Analysis*: Provides instant results based on ML model predictions.
- *Secure Backend*: API-powered backend for processing and classification.

## Tech Stack
### Frontend:
- HTML, CSS, JavaScript

### Backend:
- Node.js, Express.js

### Machine Learning Services:
- Python-based ML model for phishing detection

## Installation
### Prerequisites
- Node.js
- Python (with necessary ML libraries)

### Setup
1. Clone the repository:
   sh
   git clone https://github.com/suhass204/PhishNet_AI.git
   cd phisnet-ai
   
2. Install backend dependencies:
   sh
   npm install
   
3. Set up the ML service:
   - Ensure Python is installed.
   - Install necessary dependencies:
     sh
     pip install -r requirements.txt
     
   - Run the ML service:
     sh
     python ml_service.py
     
4. Start the backend server:
   sh
   node server.js
   
5. Open index.html in a browser to access the frontend.

## Usage
1. Enter a URL into the input field.
2. Click "Check" to analyze the link.
3. Receive instant results indicating whether the URL is phishing or legitimate.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue.

## Contact
For any inquiries, reach out at kumarvinith935@gmail.com
