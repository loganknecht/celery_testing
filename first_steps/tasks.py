"""test."""
# Python Standard Libraries
# N/A
# Third-Party Libraries
from celery import Celery
# Custom Libraries
# N/A

app = Celery(
    # The first argument to Celery is the name of the current module, this is
    # needed so that names can be automatically generated (I.E. tasks.py)
    "tasks",
    # The backend is specified via the backend argument to Celery, (or via the
    # CELERY_RESULT_BACKEND setting if you choose to use a configuration module.
    # For this example use the rpc result backend, which sends states back as
    # transient messages.
    backend="rpc://",
    # The 'broker' keyword argument specifies the URL of the message broker you
    # want to use
    broker="amqp://guest@localhost//"
)


@app.task
def add(x, y):
    """test."""
    return x + y
