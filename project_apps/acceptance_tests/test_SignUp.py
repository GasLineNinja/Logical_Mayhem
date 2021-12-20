from django.test import TestCase
from django.test import Client
from project_apps.models import Users


class SignUpSuccess(TestCase):
    def setUp(self):
        self.client = Client();

    def test_sign_up_success(self):
        response = self.client.post('signup.html', {'userName': 'ben', 'password1': '11111', 'password2': '11111',
                                                    'group': 'Administrator'})
        self.assertEqual(response.url, 'login', msg='Successfully created an account. Please log in')


class NonAdminSignUp(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = Users.objects.create(userName='ben1', password1='11111', password2='11111', firstName='Ben',
                                          lastName='Franklin', phoneNum='1234567890', email='ben1@gmail.com',
                                          group='Administrator')

    def test_sign_up_non_admin(self):
        response = self.client.post('signup.html', {'userName': 'james', 'password1': '11111', 'password2': '11111',
                                                    'group': 'Instructor'})
        self.assertEqual(response.url, 'login.html', msg='You do not have an account. '
                                                         'Contact admin to create your account.')


class UserExists(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = Users.objects.create(userName='ben1', password1='11111', password2='11111', firstName='Ben',
                                          lastName='Franklin', phoneNum='1234567890', email='ben1@gmail.com',
                                          group='Administrator')

    def test_user_exists(self):
        response = self.client.post('signup.html', {'userName': 'ben1', 'password1': '11111', 'password2': '11111',
                                                    'group': 'Administrator'})
        self.assertEqual(response.url, 'login.html', msg="You have an account. Please log in.")


class UserNameUnsuccessful(TestCase):
    def setUp(self):
        self.client = Client();

    def test_sign_up_bad_userName(self):
        response = self.client.post('signup.html', {'userName': 'ben@@)(@$s;fgjsuhfiurgodsfasdfu849tsdf394asfkfdg@@@@',
                                                    'password1': '11111', 'password2': '11111',
                                                    'group': 'Administrator'})
        self.assertEqual(response.url, 'signup.html', msg='Usernames must be a maximum of 25 characters')

    def test_sign_up_empty_userName(self):
        response = self.client.post('signup.html', {'userName': None,
                                                    'password1': '11111', 'password2': '11111',
                                                    'group': 'Administrator'})
        self.assertEqual(response.url, 'signup.html', msg='Username cannot be empty')


class PasswordUnsuccessful(TestCase):
    def setUp(self):
        self.client = Client();

    def test_sign_up_mismatch_pass(self):
        response = self.client.post('signup.html', {'userName': 'ben', 'password1': '11111', 'password2': '33333',
                                                    'group': 'Administrator'})
        self.assertEqual(response.url, 'signup.html', msg='Passwords do not match')

    def test_sign_up_one_empty_pass(self):
        response = self.client.post('signup.html', {'userName': 'ben', 'password1': '11111', 'password2': None,
                                                    'group': 'Administrator'})
        self.assertEqual(response.url, 'signup.html', msg='Passwords do not match')

    def test_sign_up_empty_pass(self):
        response = self.client.post('signup.html', {'userName': 'ben', 'password1': None, 'password2': None,
                                                    'group': 'Administrator'})
        self.assertEqual(response.url, 'signup.html', msg='passwords are empty')

    def test_sign_up_bad_password(self):
        response = self.client.post('signup.html', {'userName': 'ben', 'password1': '@./s[-3or]',
                                                    'password2': '@./s[-3or]', 'group': 'Administrator'})
        self.assertEqual(response.url, 'signup.html', response.context['message'], 'bad password',
                         msg='Error: certain characters are not allowed for the password')
