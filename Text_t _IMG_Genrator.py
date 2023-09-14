from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/data', methods=['GET'])
def getdata():
    data = "This is backend data from Flask app2"

    return (data)


if __name__ == "__main__":
    app.run(debug=True)