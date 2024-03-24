from pytz import utc

from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from utils.constant import config

db_jobstore = config.get("DB_JOB_URI", "sqlite:///jobs.sqlite")
jobstores = {
    "default": SQLAlchemyJobStore(url=db_jobstore),
}
executors = {
    "default": ThreadPoolExecutor(20),
    "processpool": ProcessPoolExecutor(5),
}
job_defaults = {
    "coalesce": False,
    "max_instances": 3,
}
scheduler = BackgroundScheduler(
    jobstores=jobstores,
    executors=executors,
    job_defaults=job_defaults,
    timezone=utc,
)

def get_scheduler():
    return scheduler
def scheduler_init():
    scheduler.start()


def shutdown_scheduler():
    scheduler.shutdown()
