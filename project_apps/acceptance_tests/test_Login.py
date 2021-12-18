from django.test import TestCase
from django.test import Client
from project_apps.models import Users


class LoginSuccess(TestCase):
    def setUp(self):
        self.client = Client();
        self.user1 = Users.objects.create(userName='ben', password1='11111', password2='11111', group='Administrator')

    def test_login_success(self):
        response = self.client.post('login.html', {'userName': 'ben', 'password1': '11111', 'password2': '11111',
                                                   'group': 'Administrator'})
        self.assertEqual(response.url, 'homepage', msg='message": "You have an account. Please log in.')

    def test_login_success_non_admin(self):
        response = self.client.post('login.html', {'userName': 'george', 'password1': '11111', 'password2': '11111',
                                                   'group': 'Instructor'})
        self.assertEqual(response.url, 'userhomepage', msg='message": "You have an account. Please log in.')


class WrongUsername(TestCase):
    def setUp(self):
        self.client = Client();
        self.user1 = Users.objects.create(userName='ben', password1='11111', password2='11111', group='Administrator')

    def test_wrong_username(self):
        response = self.client.post('login.html', {'userName': 'jack', 'password1': '11111', 'password2': '11111',
                                                   'group': 'Administrator'})
        self.assertEqual(response.url, 'login.html', response.context['message'], 'noUser',
                         msg="Username not found. Please create an account.")


class WrongPassword(TestCase):
    def setUp(self):
        self.client = Client();
        self.user1 = Users.objects.create(userName='ben', password1='11111', password2='11111', group='Administrator')

    def test_wrong_username(self):
        response = self.client.post('login.html', {'userName': 'jack', 'password1': 'hi', 'password2': 'hi',
                                                   'group': 'Administrator'})
        self.assertEqual(response.url, 'signup.html', response.context['message'], 'bad password',
                         msg="bad password")
