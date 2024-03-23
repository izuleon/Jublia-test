from flask import Flask, redirect, url_for

from route import event_mail

app = Flask(__name__)

app.register_blueprint(event_mail.event_mail_bp)


@app.route("/")
def index():
    return "hello world"


@app.route("/save_emails")
def redirect_and_save_emails():
    return redirect(url_for("event_mail.save_emails"))


if __name__ == "__main__":
    app.run(debug=True)
