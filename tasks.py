"""test."""
# Python Standard Libraries
# N/A
# Third-Party Libraries
from celery import Celery
# Custom Libraries
# N/A

app = Celery('tasks', broker='amqp://guest@localhost//')


@app.task
def add(x, y):
    """test."""
    return x + y
