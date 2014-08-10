from __future__ import absolute_import

from task_launcher.celery_app import app


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


@app.task
def delay(d):
    import time
    time.sleep(d)
    return d


@app.task
def time():
    import datetime
    return datetime.datetime.now()


@app.task
def complex_method(d):
    d_inverse = d
    for k, v in d.iteritems():
        print k, v
        d_inverse[v] = k


@app.task
def call_method():
    return time()


@app.task
def raise_exception():
    raise RuntimeError("Excepcion de prueba")