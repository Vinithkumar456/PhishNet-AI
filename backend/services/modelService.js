const axios = require('axios');

exports.getPhishingPrediction = async (url) => {
    try {
        const flaskAPI = 'http://127.0.0.1:5000/predict';

        const response = await axios.post(flaskAPI, { url });

        console.log("Flask API Response:", response.data);

        return response.data.prediction;  // Directly return the model's output

    } catch (error) {
        console.error("Error calling Flask API:", error.message);
        throw new Error("Flask API call failed");
    }
};
