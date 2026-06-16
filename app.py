from flask import Flask, request
import requests

app = Flask(__name__)

VERIFY_TOKEN = "vikky123"
ACCESS_TOKEN = "IGAAV4a0BpFx9BZAGFTSHB1aVFoOVc5SkhlVHk1U0ZAfelZA3WHZArdjlJcF9SQlFRcjlRcUtwdmhyS2Nlc09scFhESHV6RHdvWXJQM0RPLThYSUpGZAkx3VkNkZAlFIVDZAHaUJRZAjBESXlvNy1CaTlUSVFyTUk5TzN3ODJJV2VucWJnSQZDZD"


@app.route("/")
def home():
    return "Bot Running"


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

    data = request.json

    print(data)

    try:

        for entry in data.get("entry", []):

            for change in entry.get("changes", []):

                value = change.get("value", {})

                comment_id = value.get("id")

                if comment_id:

                    requests.post(
                        f"https://graph.facebook.com/v23.0/{comment_id}/replies",
                        data={
                            "message": "Please WhatsApp us on 8431995310 for pricing and ordering details.",
                            "access_token": ACCESS_TOKEN
                        }
                    )

    except Exception as e:
        print("ERROR:", e)

    return "EVENT_RECEIVED", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)