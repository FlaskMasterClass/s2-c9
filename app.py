import os
import pathlib
import random

import flask
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import current_app
from flask import flash
import click
from flask_mailman import EmailMessage


from init import mail

from flask.cli import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)


from config import ProductionConfig
from config import DevelopmentConfig
from config import TestingConfig


profiles = {
    "development": DevelopmentConfig(),
    "production": ProductionConfig(),
    "testing": TestingConfig(),
}




def create_app(profile):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(profiles[profile])
    app.config.from_pyfile("config.py", silent=True)
    app.config["SECRET_KEY"] = os.urandom(24)

    mail.init_app(app)

    if profile != "testing":
        app.config.from_pyfile("config.py", silent=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    return app


flask_env = os.environ.get("FLASK_ENV", default="development")
app = create_app(flask_env)

if __name__ == "__main__":

    @app.route("/send-mail", methods=["GET", "POST"])
    def home():
        msg = EmailMessage(
            f'Hello Test {random.randint(0, 100)}',
            f"You choose {random.choice(['Mango', 'Pear'])}",
            'from@educative.example',
            ['to1@educative.example', 'to2@educative.example'],
            ['bcc@educative.example'],
            reply_to=['another@example.com'],
            headers={'Message-ID': 'foo'},
        )
        msg.send()
        return 'sending mail ...'

    app.run(host="0.0.0.0", port=5012, debug=True, ssl_context='adhoc')
