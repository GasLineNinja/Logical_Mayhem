from django.test import TestCase
from django.test import Client
from project_apps.models import Users


class LoginSuccess(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = Users.objects.create(userName='ben1', password1='11111', password2='11111', firstName='Ben',
                                          lastName='Franklin', phoneNum='1234567890',
                                          email='ben1@gmail.com', group='Administrator')
        self.user2 = Users.objects.create(userName='jack1', password='12345', password2='12345', firstName='Jack',
                                          lastName='Thomas', phoneNum='1234567890',
                                          email='jack1@gmail.com', group="Instructor")

    def test_login_success_admin(self):
        response = self.client.post('login.html', {'userName': 'ben1', 'password1': '11111'})
        self.assertEqual(response.url, 'homepage', msg='message": "Login Successful.')

    def test_login_success_non_admin(self):
        response = self.client.post('login.html', {'userName': 'jack1', 'password1': '12345'})
        self.assertEqual(response.url, 'userhomepage', msg='Login Successful')


class NonExistingUser(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = Users.objects.create(userName='ben1', password1='11111', password2='11111', firstName='Ben',
                                          lastName='Franklin', phoneNum='1234567890',
                                          email='ben1@gmail.com', group='Administrator')

    def test_no_user(self):
        response = self.client.post('login.html', {'userName': 'jack', 'password1': '16543'})
        self.assertEqual(response.url, 'signup.html', msg='Username not found. Please create an account.')


class WrongUsername(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = Users.objects.create(userName='ben1', password1='11111', password2='11111', firstName='Ben',
                                          lastName='Franklin', phoneNum='1234567890',
                                          email='ben1@gmail.com', group='Administrator')

    def test_empty_username(self):
        response = self.client.post('login.html', {'userName': None, 'password1': '11111'})
        self.assertEqual(response.url, 'login.html', msg='Username cannot be empty')


class WrongPassword(TestCase):
    def setUp(self):
        self.client = Client();
        self.user1 = Users.objects.create(userName='ben1', password1='11111', password2='11111', firstName='Ben',
                                          lastName='Franklin', phoneNum='1234567890',
                                          email='ben1@gmail.com', group='Administrator')

    def test_wrong_password(self):
        response = self.client.post('login.html', {'userName': 'ben1', 'password1': 'hi'})
        self.assertEqual(response.url, 'login.html', response.context['message'], 'bad password',
                         msg='Error: password is incorrect')

    def test_empty_password(self):
        response = self.client.post('login.html', {'userName': 'ben1', 'password1': None})
        self.assertEqual(response.url, 'login.html', response.context['message'], 'bad password',
                         msg='Password cannot be empty')
