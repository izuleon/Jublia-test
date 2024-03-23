import os

from dotenv import dotenv_values
from flask import Flask

from route import event_mail, index

config = {
    **dotenv_values(".env.shared"),  # load shared development variables
    **dotenv_values(".env.secret"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}

app = Flask(__name__)

app.register_blueprint(event_mail.event_mail_bp)
app.register_blueprint(index.index_bp)


if __name__ == "__main__":
    app.run(debug=True)
