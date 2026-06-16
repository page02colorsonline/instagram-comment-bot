from flask import Flask, request
import requests

app = Flask(__name__)

VERIFY_TOKEN = "vikky123"

ACCESS_TOKEN = "PASTE_YOUR_ACCESS_TOKEN_HERE"


@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200

    return "Verification failed", 403


@app.route("/webhook", methods=["POST"])
def webhook():

    print(request.json)

    return "EVENT_RECEIVED", 200


@app.route("/")
def home():
    return "Bot Running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)