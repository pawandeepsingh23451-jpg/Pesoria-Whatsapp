from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "Pesoria_WA_2026"

@app.route("/webhook", methods=["GET"])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if token == VERIFY_TOKEN:
        return challenge, 200

    return "Invalid verify token", 403


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print(data)

    return "EVENT_RECEIVED", 200
