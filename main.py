
from flask import Flask, render_template_string
import random

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>A Little Invitation 💗</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #ffb6c1, #ffc0cb, #ffe4e1);
    overflow: hidden;
    text-align: center;
}

.card {
    background: white;
    width: 90%;
    max-width: 420px;
    padding: 30px 20px;
    border-radius: 25px;
    box-shadow: 0 10px 30px #0002;
    position: relative;
}

h1 {
    color: #ff4f87;
    font-size: 27px;
}

.names {
    color: #777;
    line-height: 1.7;
    font-size: 15px;
}

.heart {
    font-size: 55px;
    animation: beat 1s infinite;
}

@keyframes beat {
    50% { transform: scale(1.2); }
}

.buttons {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 30px;
    min-height: 55px;
}

button {
    border: none;
    border-radius: 30px;
    padding: 13px 25px;
    font-size: 17px;
    font-weight: bold;
    cursor: pointer;
}

#yes {
    background: #ff4f87;
    color: white;
}

#no {
    background: #ddd;
    color: #444;
    position: relative;
}

#message {
    color: #ff4081;
    font-weight: bold;
    margin-top: 25px;
    font-size: 18px;
}

.float {
    position: absolute;
    bottom: -30px;
    animation: floatUp 6s linear infinite;
    pointer-events: none;
}

@keyframes floatUp {
    to {
        transform: translateY(-110vh) rotate(360deg);
        opacity: 0;
    }
}
</style>
</head>

<body>

<div class="card">
    <div class="heart">💗</div>

    <p class="names">
        To: <b>Christian Raphael Paraiso Segui</b><br>
        From: <b>Xiannnn😛</b>
    </p>

    <h1>Will you go out with me? 🥺</h1>
    <p>You have one very important question to answer...</p>

    <div class="buttons">
        <button id="yes" onclick="sayYes()">YES 💗</button>
        <button id="no" onpointerenter="tryNo()">NO 😭</button>
    </div>

    <div id="message"></div>
</div>

<script>
let attempts = 0;

function moveNoButton() {
    const no = document.getElementById("no");

    no.style.position = "fixed";
    no.style.left = Math.random() * (window.innerWidth - no.offsetWidth) + "px";
    no.style.top = Math.random() * (window.innerHeight - no.offsetHeight) + "px";
}

function tryNo() {
    attempts++;

    if (attempts >= 2) {
        document.getElementById("message").innerHTML =
            "Under the button, are you sure about that? 👀😭";
    } else {
        document.getElementById("message").innerHTML =
            "HEY! You almost got it! 😭";
    }

    moveNoButton();
}

function sayYes() {
    document.getElementById("message").innerHTML =
        "YIPPEEE YESS FINALLY I'VE BEEN WAITING FOR THIS!!! 💗🎉";

    document.getElementById("no").style.display = "none";

    document.querySelector("h1").innerHTML =
        "THE ANSWER IS YES!!! 💕";
}

// Floating hearts
setInterval(() => {
    const heart = document.createElement("div");
    heart.className = "float";
    heart.innerHTML = ["💗", "💕", "💖", "💘"][
        Math.floor(Math.random() * 4)
    ];
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.fontSize = (18 + Math.random() * 20) + "px";
    document.body.appendChild(heart);

    setTimeout(() => heart.remove(), 6000);
}, 500);
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
