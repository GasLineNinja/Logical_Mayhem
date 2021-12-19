from django.test import TestCase
from django.test import Client
from project_apps.models import Users


class SignUpSuccess(TestCase):
    def setUp(self):
        self.client = Client();

    def test_sign_up_success(self):
        response = self.client.post('signup.html', {'userName': 'george', 'password1': '11111', 'password2': '11111',
                                                    'group': 'Administrator'})
        self.assertEqual(response.url, 'login', msg='message": "You have an account. Please log in.')


class PasswordUnsuccessful(TestCase):
    def setUp(self):
        self.client = Client();

    def test_sign_up_mismatch_pass(self):
        response = self.client.post('signup.html', {'userName': 'george', 'password1': '11111', 'password2': '33333',
                                                    'group': 'Administrator'})
        self.assertEqual(response.url, 'signup.html', msg='Passwords do not match')

    def test_sign_up_bad_password(self):
        response = self.client.post('signup.html', {'userName': 'george', 'password1': '@./s[-3or]',
                                                    'password2': '@./s[-3or]', 'group': 'Administrator'})
        self.assertEqual(response.url, 'signup.html', response.context['message'], 'bad password',
                         msg='Error: User must add a password to create an account')


