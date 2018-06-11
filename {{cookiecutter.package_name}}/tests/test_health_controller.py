from unittest import TestCase

from {{cookiecutter.package_name}}.controllers.health_controller import HealthController

class TestHealthController(TestCase):

    def setUp(self):
        self.health_controller = HealthController()

    def test_live_status(self):
        self.assertEqual(self.health_controller.live(), 'OK')

    def test_ready_status(self):
        self.assertEqual(self.health_controller.ready(), 'OK')