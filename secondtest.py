from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, everybody. Step 1. Step 2'

app.run(host='0.0.0.0', port=8080)
