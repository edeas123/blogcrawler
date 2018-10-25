from blogcrawler.config import load_config

# load configurations
_config = load_config()

broker_url = _config.MESSAGE_BROKER_HOST
result_backend = _config.REDIS_URL
include = ['blogcrawler.celery.tasks']
beat_schedule: dict = {}
task_queues = None
worker_redirect_stdouts_level = 'DEBUG'
