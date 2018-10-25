from celery import Celery

app = Celery('blogcrawler')

# set app config
app.config_from_object('blogcrawler.celery.celeryconfig')

# main
if __name__ == '__main__':
    app.worker_main()
