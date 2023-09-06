from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def increment_endpoint():
    data = request.get_json()
    
    if 'number' in data:
        try:
            number = int(data['number'])
            result = number + 1
            return jsonify({"result": result})
        except ValueError:
            return jsonify({"error": "Invalid input, 'number' must be an integer"}), 400
    else:
        return jsonify({"error": "'number' not found in request data"}), 400


@app.route('/get', methods=['GET'])
def get_endpoint():
    return jsonify(
        {"message": "GET message"}
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)