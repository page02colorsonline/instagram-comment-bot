from flask import Flask, request
import requests

app = Flask(**name**)

VERIFY_TOKEN = "vikky123"
ACCESS_TOKEN = "IGAAV4a0BpFx9BZAGFncXVlSDk4d2tVaVhmb2JESDFfRjVNNEFmTmpjS1FJbEVULUVWLWkza1k3Y2VOdXZA2YlVqVVJpcUpfa0xteS1ReVFLYjBmNWJnT1RMSkZArbk1vOHBnYUFHWWlvZAzhXcnZAFaWU0em5LV2VEaC13NE1pcUh4RQZDZD"

REPLY_MESSAGE = "Please WhatsApp us on 8431995310 for pricing and ordering details."

@app.route("/")
def home():
return "Bot Running"

@app.route("/webhook", methods=["GET"])
def verify():
mode = request.args.get("hub.mode")
token = request.args.get("hub.verify_token")
challenge = request.args.get("hub.challenge")

```
if mode == "subscribe" and token == VERIFY_TOKEN:
    return challenge, 200

return "Verification failed", 403
```

@app.route("/webhook", methods=["POST"])
def webhook():

```
data = request.json
print(data)

try:
    for entry in data.get("entry", []):

        for change in entry.get("changes", []):

            value = change.get("value", {})

            comment_id = value.get("id")

            if not comment_id:
                continue

            response = requests.post(
                f"https://graph.facebook.com/v23.0/{comment_id}/replies",
                data={
                    "message": REPLY_MESSAGE,
                    "access_token": ACCESS_TOKEN
                }
            )

            print("Reply Status:", response.status_code)
            print("Reply Response:", response.text)

except Exception as e:
    print("ERROR:", e)

return "EVENT_RECEIVED", 200
```

if **name** == "**main**":
app.run(host="0.0.0.0", port=5000)
