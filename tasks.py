import time
from celery import Celery

# app = Celery('tasks', broker='pyamqp://guest@localhost')


aa = Celery(
    'tasks',
    backend='rpc://',
    broker='pyampq://guest@localhost//'
)


@app.task
def add(x, y):
    time.sleep(10)
    return x + y