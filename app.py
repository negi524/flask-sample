from flask import Flask
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
