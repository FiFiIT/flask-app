import time
from flask_cors import CORS
from flask import Flask, jsonify, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'E:/Nauka/FLASK/pictures'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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
    {
        "name": "Alien",
        "url": "C:/Users/filip/OneDrive/Pictures/xcom.jpg"
    }
]


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/tinderCards')
def get_tinderCards():
    return jsonify(tinderCards)


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/home/<string:name>/age/<int:age>')
def sayHello(name, age):
    return f"Hello {name} your age is {age}"


if __name__ == "__main__":
    app.run(host='192.168.0.48', debug=True)
