from blogcrawler.celery.app import app


@app.task()
def addition(a, b):
    return a + b

