const express = require('express');
const { predictPhishing } = require('../controllers/predictionController');

const router = express.Router();

router.post('/predict', predictPhishing);

module.exports = router;
