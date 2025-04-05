const { getPhishingPrediction } = require('../services/modelService');

exports.predictPhishing = async (req, res) => {
    try {
        const { url } = req.body;

        if (!url) {
            return res.status(400).json({ error: 'URL is required' });
        }

        // Call the Flask API to get prediction
        const prediction = await getPhishingPrediction(url);

        res.json({
            url,
            prediction
        });

    } catch (error) {
        res.status(500).json({ error: 'Server Error', details: error.message });
    }
};
