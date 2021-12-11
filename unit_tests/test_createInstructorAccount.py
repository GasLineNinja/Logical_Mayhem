import unittest
#test for if preconditions aren't met, test if they are
#test if conditions are given something they aren't expecting
#look for holes
from django.contrib.auth.models import User
from django.test import Client

from project_apps.models import createAccount


class TestGetAccount(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.account1 = createAccount.objects.create( createNewAccount= "true", createUser = 'JasonRock', createPassword = '123',  generateUserid= '2468')
        self.account2 = createAccount.objects.create( createNewAccount= "false", createUser = 'JasonRock', createPassword = '123',  generateUserid= '2468')
    def test_falseCreateNewAccount(self):
        pass

    def test_trueCreateNewAccount(self):
        pass

    def test_adminRequest(self):
        pass

    def test_notAdminRequest(self):
        pass

    def test_accountCreated(self):
        pass

    def test_accountNotCreated(self):
        pass

class TestCreateAccount(unittest.TestCase):
    def setUp(self):
        pass

    def test_getAccountNotTrue(self):
        pass

    def test_getAccountTrue(self):
        pass

    def test_createNewAccountTATrue(self):
        pass

    def test_createNewAccountInstructorTrue(self):
        pass

    def test_createNewAccountTAcreateNewAccountInstructorFalse(self):
        pass

    def test_createNewAccountTAcreateNewAccountInstructorTrue(self):
        pass

    def test_newInstructorcreated(self):
        pass

    def test_newInstructorNotCreated(self):
        pass

    def test_newUsernameGenerated(self):
        pass

    def test_newUsernameNotGenerated(self):
        pass

    def test_newPasswordGenerated(self):
        pass

    def test_newPasswordNotGenerated(self):
        pass

class test_SaveAccount(unittest.TestCase):
    def test_usernameNotValid(self):
        pass

    def test_passwordNotValid(self):
        pass

    def test_usernamePasswordNotValid(self):
        pass

    def test_usernamePasswordValid(self):
        pass

    def test_userIDMatchesUsernamePassword(self):
        pass

    def test_userIDNotMatchesUsernamePassword(self):
        pass