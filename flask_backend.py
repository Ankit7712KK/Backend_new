from flask import Flask, jsonify
from flask_cors import CORS
import cohere

app = Flask(__name__)
CORS(app)


@app.route('/api/data', methods=['GET'])
def getdata():
    data = "This is backend data from Flask application"
    prmpt = "Indian constitution"
    co = cohere.Client('sDeY1e2YtCt3XOdGOxZgDecF2H9I108rwdLy6Emw')
    response = co.generate(
        model='e6366bc6-735b-4654-a319-5d4dd1fea947-ft',
        prompt=prmpt,
        max_tokens=300)
    print('Prediction: {}'.format(response.generations[0].text))
    return (data)


if __name__ == "__main__":
    app.run(debug=True)