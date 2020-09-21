import time
from flask_cors import CORS
from flask import Flask, jsonify

app = Flask(__name__)
cors = CORS(app)


tinderCards = [
    {
        "name": "Kotek",
        "url": "Karpacz//IMG_20200704_120039.jpg",
    },
    {
        "name": "Tobiaszek",
        "url": "Karpacz//IMG_20200815_182037.jpg",
    },
    {
        "name": "Citoren",
        "url": "Karpacz//IMG_20200826_100346.jpg",
    },
]


@app.route('/')
def hello():
    return jsonify(tinderCards)


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/home/<string:name>/age/<int:age>')
def sayHello(name, age):
    return f"Hello {name} your age is {age}"


if __name__ == "__main__":
    app.run(debug=True)
