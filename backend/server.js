const express = require('express');
const cors = require('cors');
require('dotenv').config();
const predictionRoutes = require('./routes/predictionRoutes');

const app = express();

app.use(cors());
app.use(express.json());

app.use('/api', predictionRoutes);

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

