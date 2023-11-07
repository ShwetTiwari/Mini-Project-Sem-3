from flask import Flask, request, jsonify
import time

app = Flask(__name__)

data_store = []

@app.route('/data', methods=['POST'])
def handle_data():
    received_data = request.get_json()
    data_store.append(received_data)
    return jsonify({"message": "Data received successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)