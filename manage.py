from db.base_db import db_session
from route import event_mail, index, recipient
from utils.config import get_app
from utils.scheduler_init import scheduler_init, shutdown_scheduler

app = get_app()

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
