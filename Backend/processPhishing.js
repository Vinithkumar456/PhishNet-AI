const { spawn } = require("child_process");

module.exports.checkPhishing = (url, callback) => {
    // Call the Python script and pass the URL to it
    const python = spawn("python", ["../Python/phising_model.py", url]);

    python.stdout.on("data", (data) => {
        callback(data.toString());
    });

    python.stderr.on("data", (data) => {
        console.error(`stderr: ${data}`);
    });

    python.on("close", (code) => {
        if (code !== 0) {
            console.log(`Python process exited with code ${code}`);
        }
    });
};
