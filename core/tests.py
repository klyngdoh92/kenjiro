from django.test import TestCase


class BasicTest(TestCase):
    def test_health(self):
        self.assertEqual(1, 1)
