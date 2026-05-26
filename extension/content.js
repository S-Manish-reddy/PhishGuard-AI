console.log("PhishGuard AI Loaded");

let lastEmailText = "";

// Create/update banner
function showBanner(message, color) {

    let banner = document.getElementById("phishguard-banner");

    // Create banner if not exists
    if (!banner) {

        banner = document.createElement("div");

        banner.id = "phishguard-banner";

        banner.style.position = "fixed";
        banner.style.top = "20px";
        banner.style.right = "20px";
        banner.style.zIndex = "999999";
        banner.style.padding = "15px 20px";
        banner.style.fontSize = "16px";
        banner.style.fontWeight = "bold";
        banner.style.borderRadius = "12px";
        banner.style.color = "white";
        banner.style.fontFamily = "Arial, sans-serif";
        banner.style.boxShadow = "0 4px 10px rgba(0,0,0,0.3)";

        document.body.appendChild(banner);
    }

    banner.style.backgroundColor = color;
    banner.innerText = message;
}

// Detect currently opened email
function detectEmail() {

    // Gmail email body selector
    const emailElement = document.querySelector(".a3s");

    if (!emailElement) {
        return;
    }

    const emailText = emailElement.innerText.trim();

    // Avoid rescanning same email
    if (
        emailText.length < 50 ||
        emailText === lastEmailText
    ) {
        return;
    }

    lastEmailText = emailText;

    console.log("Scanning Email...");

    // Temporary scanning banner
    showBanner("PhishGuard AI: Scanning Email...", "#1a73e8");

    // Send to Flask backend
    fetch("http://127.0.0.1:5000/predict", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            email: emailText
        })

    })

    .then(response => response.json())

    .then(data => {

        console.log("Prediction:", data);

        let message = "";
        let color = "";

        // Smarter confidence interpretation

        if (
            data.prediction === "High Risk Phishing"
            && data.confidence >= 85
        ) {

            message =
                `🚨 High Risk Phishing (${data.confidence}%)`;

            color = "#d93025";

        }

        else if (
            data.prediction === "Suspicious Email"
        ) {

            message =
                `⚠️ Suspicious Email (${data.confidence}%)`;

            color = "#f9ab00";

        }

        else if (
            data.confidence >= 85
        ) {

            message =
                `✅ Safe Email (${data.confidence}%)`;

            color = "#188038";

        }

        else {

            message =
                `❓ Uncertain Email (${data.confidence}%)`;

            color = "#5f6368";
        }

        showBanner(message, color);

    })

    .catch(error => {

        console.error("PhishGuard Error:", error);

        showBanner(
            "Backend Connection Failed",
            "#d93025"
        );
    });
}

// Continuously monitor Gmail
setInterval(detectEmail, 3000);