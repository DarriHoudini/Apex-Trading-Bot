
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    print("Received data:", data)  # This prints to Render logs for now
    return jsonify({'status': 'received'}), 200

@app.route('/', methods=['GET'])
def home():
    return "GreaseV1 Webhook Receiver Active", 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)
