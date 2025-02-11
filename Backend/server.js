const express = require("express");
const bodyParser = require("body-parser");
const processPhishing = require("./processPhishing");
const cors = require('cors');

const app = express();
const port = 5000;
app.use(cors());

app.use(bodyParser.json());

app.post("/check-url", (req, res) => {
    const url = req.body.url;

    processPhishing.checkPhishing(url, (result) => {
        res.json({ result: result });
    });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
