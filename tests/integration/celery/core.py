import unittest
from subprocess import run


class CeleryTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # start the celery worker to listen for task
        run([
            "celery", "worker",
            "--detach",
            "-A", "blogcrawler.celery.app.app"
        ])

    @classmethod
    def tearDownClass(cls):
        # kill the celery worker
        run([
            "celery",
            "-A", "blogcrawler.celery.app.app",
            "control", "shutdown"
        ])
