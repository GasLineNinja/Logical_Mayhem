from django.test import TestCase
from django.test import Client
from project_apps.models import Users, Courses, Labs


class TestCreateAccount(TestCase):
    def success(self):
        self.assertEqual(True, False)  # add assertion here

    def failure(self):
        self.assertequal(True, False)


