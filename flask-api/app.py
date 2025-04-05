
from flask import Flask, request, jsonify
import pickle
import pandas as pd
from feature_extraction import extract_features # Ensure this function is imported

app = Flask(__name__)

# Load trained model
with open("models/xgboost_model.pkl", "rb") as f:
    model = pickle.load(f)

import xgboost as xgb


import numpy as np

FEATURE_NAMES = [
    "url_length", "num_dots", "num_hyphens", "num_slashes",
    "num_digits", "has_https", "has_www", "domain_length",
    "special_chars", "is_ip"
]

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Extract features
    features = extract_features(data['url'])  # Should return a list/array
    
    # Debugging output
    print("Extracted Features:", features)
    print("Type of extracted features:", type(features))
    
    # Ensure features are converted into a Pandas DataFrame with column names
    if isinstance(features, list) or isinstance(features, np.ndarray):
        df = pd.DataFrame([features], columns=FEATURE_NAMES)  # Create DataFrame with correct names
    else:
        raise ValueError("Feature extraction did not return a valid list or array!")

    print("Final DataFrame Shape:", df.shape)
    print("Final DataFrame Columns:", df.columns.tolist())

    # Convert to XGBoost DMatrix
    dmatrix = xgb.DMatrix(df, feature_names=FEATURE_NAMES)

    # Perform prediction
    prediction = model.predict(dmatrix)[0]
    print("Debug - Raw Model Prediction:", prediction)


    return jsonify({
        "url": data['url'],
        "prediction": "bad" if prediction >= 0.95 else "good"
    })




if __name__ == "__main__":
    app.run(debug=True)