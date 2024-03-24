from flask import Flask
from werkzeug.serving import WSGIRequestHandler

from db.base_db import db_session, init_db
from route import event_mail, index

app = Flask(__name__)

app.register_blueprint(event_mail.event_mail_bp)
app.register_blueprint(index.index_bp)

# WSGIRequestHandler.sigterm_handler = shutdown_scheduler
# WSGIRequestHandler.sighup_handler = shutdown_scheduler


if __name__ == "__main__":
    app.run(debug=True)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
