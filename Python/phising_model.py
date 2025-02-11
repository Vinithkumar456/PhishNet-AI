import pickle
import sys
import pandas as pd
from urllib.parse import urlparse

# Load trained model
with open("phishing_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Extract features
def extract_features(url):
    parsed_url = urlparse(url)
    features = {
        'length_url': len(url),
        'length_hostname': len(parsed_url.netloc),
        'nb_dots': url.count("."),
        'nb_hyphens': url.count("-")
    }
    return features

# Function to check if a URL is phishing
def check_phishing(url):
    features = extract_features(url)
    feature_df = pd.DataFrame([features])

    # Predict
    prediction = model.predict(feature_df)

    return prediction

# Run detection
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python phishing_model.py <url>")
        sys.exit(1)
    
    url = sys.argv[1]
    result = check_phishing(url)
    print(result)
