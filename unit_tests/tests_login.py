from django.test import TestCase
from django.test import Client
from project_apps.models import Users

class Test_Login(TestCase):
    def setup(self):
        self.client = Client()
        self.users = Users.object.create(userName='user1', password1='password')

    def test_successfulLogin(self):
        response = self.client.post('/', {'name:', 'user1', 'password:', 'password'})
        self.assertEquals(response.url, "/userHomePage/")

    def test_unsuccessfulLogin(self):
        response = self.client.post('/', {'name:', 'user1', 'password:', 'password'})
        self.assertEqual(response.context['message'], "bad password")
