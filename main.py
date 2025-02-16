from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get('message', 'No message received')
    return jsonify({"Received": message}), 200

if __name__ == '__main__':
    app.run(debug=True)
