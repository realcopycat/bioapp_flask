from celery import Celery

from entrance.config import celery as config
from entrance.config.celery import broker_url

celery = Celery(__name__, broker=broker_url)


def register_celery(app):
    celery.config_from_object(config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask

