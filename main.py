from flask import Flask, request
app = Flask(__name__)
VERIFY_TOKEN = "elkady_2026_verify"

@app.route('/')
def home():
    return "Bot is Running!"

@app.route('/webhook', methods=['GET'])
def verify():
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if token == VERIFY_TOKEN:
        return challenge
    return "error", 403

@app.route('/webhook', methods=['POST'])
def webhook():
    print(request.get_json())
    return "ok", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)