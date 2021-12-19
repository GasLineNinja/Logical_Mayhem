from django.test import TestCase
from django.test import Client
from project_apps.models import Users


class AddUserSuccess(TestCase):
    def setUp(self):
        self.client = Client()

    def test_add_user_success_admin(self):
        response = self.client.post('addUsers.html', {'userName': 'ben1', 'firstName': 'Ben', 'lastName': 'Franklin',
                                                      'email': "benf@gmail.com", 'password1': '11111',
                                                      'group': 'Administrator'})
        self.assertEqual(response.url, 'addusers', msg='user added successfully')

    def test_add_user_success_non_admin(self):
        response = self.client.post('addUsers.html', {'userName': 'jack1', 'firstName': 'Jack', 'lastName': 'Thomas',
                                                      'email': "jack1@gmail.com", 'password1': '12345',
                                                      'group': 'Instructor'})
        self.assertEqual(response.url, 'addusers', msg='Login Successful')


class AddUserSuccessWithUsers(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = Users.objects.create(userName='ben1', password1='11111', password2='11111', firstName='Ben',
                                          lastName='Franklin', phoneNum='1234567890',
                                          email='ben1@gmail.com', group='Administrator')
        self.user2 = Users.objects.create(userName='jack1', password='12345', password2='12345', firstName='Jack',
                                          lastName='Thomas', phoneNum='1234567890',
                                          email='jack1@gmail.com', group='Instructor')

    def test_add_user_success_admin_existing_users(self):
        response = self.client.post('addUsers.html', {'userName': 'pen1', 'firstName': 'Pen', 'lastName': 'Drew',
                                                      'email': "pend@gmail.com", 'password1': '00000',
                                                      'group': 'Administrator'})
        self.assertEqual(response.url, 'addusers', msg='user added successfully')

    def test_add_user_success_non_admin_existing_users(self):
        response = self.client.post('addUsers.html', {'userName': 'and123', 'firstName': 'Andrew', 'lastName': 'Salmon',
                                                      'email': "and1@gmail.com", 'password1': '123455',
                                                      'group': 'Instructor'})
        self.assertEqual(response.url, 'addusers', msg='Login Successful')


class UserExists(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = Users.objects.create(userName='ben1', password1='11111', password2='11111', firstName='Ben',
                                          lastName='Franklin', phoneNum='1234567890',
                                          email='ben1@gmail.com', group='Administrator')

    def test_existing_user(self):
        response = self.client.post('addUsers.html', {'userName': 'ben1', 'firstName': 'Ben', 'lastName': 'Franklin',
                                                      'email': "benf@gmail.com", 'password1': '11111',
                                                      'group': 'Administrator'})
        self.assertEqual(response.url, 'addUsers.html', msg='this user already exists')


class AddUserMissingElements(TestCase):
    def setUp(self):
        self.client = Client()

    def test_add_user_empty_userName(self):
        response = self.client.post('addUsers.html', {'userName': None, 'firstName': 'Ben', 'lastName': 'Franklin',
                                                      'email': "benf@gmail.com", 'password1': '11111',
                                                      'group': 'Administrator'})
        self.assertEqual(response.url, 'addUsers.html', msg='Must add userName to add user')

    def test_add_user_empty_firstName(self):
        response = self.client.post('addUsers.html', {'userName': 'ben1', 'firstName': None, 'lastName': 'Franklin',
                                                      'email': "benf@gmail.com", 'password1': '11111',
                                                      'group': 'Administrator'})
        self.assertEqual(response.url, 'addUsers.html', msg='Must add firstName to add user')

    def test_add_user_empty_lastName(self):
        response = self.client.post('addUsers.html', {'userName': 'ben1', 'firstName': 'Ben', 'lastName': None,
                                                      'email': "benf@gmail.com", 'password1': '11111',
                                                      'group': 'Administrator'})
        self.assertEqual(response.url, 'addUsers.html', msg='Must add lastName to add user')

    def test_add_user_empty_email(self):
        response = self.client.post('addUsers.html', {'userName': 'ben1', 'firstName': 'Ben', 'lastName': 'Franklin',
                                                      'email': None, 'password1': '11111',
                                                      'group': 'Administrator'})
        self.assertEqual(response.url, 'addUsers.html', msg='Must add email to add user')

    def test_add_user_empty_password(self):
        response = self.client.post('addUsers.html', {'userName': 'ben1', 'firstName': 'Ben', 'lastName': 'Franklin',
                                                      'email': 'benf@gmail.com', 'password1': None,
                                                      'group': 'Administrator'})
        self.assertEqual(response.url, 'addUsers.html', msg='Must add password to add user')

    def test_add_user_empty_group(self):
        response = self.client.post('addUsers.html', {'userName': 'ben1', 'firstName': 'Ben', 'lastName': 'Franklin',
                                                      'email': 'benf@gmail.com', 'password1': '11111',
                                                      'group': None})
        self.assertEqual(response.url, 'addUsers.html', msg='Must add group to add user')
