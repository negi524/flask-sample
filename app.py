from flask import Flask, render_template
import logging
import logging.config
import yaml

app = Flask(__name__)

response = {"userId": 1, "userName": "hoge"}

# ログ設定読み込み
with open("./logsetting.yml", "r") as file:
    logging.config.dictConfig(yaml.safe_load(file))


@app.route("/")
def hello_world():
    app.logger.info("info log.")
    return response


@app.route("/user/<username>/")
def show_user_name(username: str):
    return render_template("hello.html", userName=username)


@app.route("/about/")
def show_about_page():
    return {"pageName": "about"}
