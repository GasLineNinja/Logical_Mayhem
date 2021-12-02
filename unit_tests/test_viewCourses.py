from django.test import TestCase
from django.test import Client
from project_apps.models import Users, Courses, Labs

class MyTestCase(TestCase):
    def setup(self):
        self.client = Client();

        self.user1 = Users.objects.create()
