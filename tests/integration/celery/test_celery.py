from tests.integration.celery.core import CeleryTestCase
from blogcrawler.celery.tasks import addition


class TestCeleryTask(CeleryTestCase):

    def test_addition(self):

        self.assertEqual(addition(3, 5), 8)
        self.task = addition.apply_async(args=[3, 5])
        self.results = self.task.get(timeout=5)
        self.assertEqual(self.task.state, 'SUCCESS')
