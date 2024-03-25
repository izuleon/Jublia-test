from flask import Flask
from flask_mail import Mail

from utils.constant import config as env_config

app = Flask(__name__)
app.config.from_mapping(env_config)
mail = Mail(app)


def get_app():
    return app


def get_mail():
    return mail
