from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/data', methods=['GET'])
def data():
    return jsonify({"data": [1, 2, 3, 4, 5]})

@app.route('/api/foo', methods=['GET'])
def foo():
    return jsonify({"message": "Hello, Foo"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
