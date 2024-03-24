from flask import Flask

from email_scheduler.scheduler_init import scheduler_init, shutdown_scheduler
from db.base_db import db_session
from route import event_mail, index, recipient

app = Flask(__name__)

app.register_blueprint(event_mail.event_mail_bp)
app.register_blueprint(recipient.recipient_bp)
app.register_blueprint(index.index_bp)


if __name__ == "__main__":
    scheduler_init()
    app.run(debug=True)


@app.teardown_appcontext
def shutdown_session(exception=None):
    shutdown_scheduler()
    db_session.remove()
