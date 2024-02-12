from flask import Flask

app = Flask(__name__)

response = {"userId": 1, "userName": "hoge"}


@app.route("/")
def hello_world():
    app.logger.info("info log.")
    return response
