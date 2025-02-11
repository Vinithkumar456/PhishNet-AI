function checkPhishing() {
    const url = document.getElementById("urlInput").value;
    
    if (url) {
        fetch(`http://localhost:5000/check-url`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ url: url }),
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText = `Result: ${data.result}`;
        })
        .catch(error => {
            console.error("Error:", error);
        });
    } else {
        alert("Please enter a URL.");
    }
}
