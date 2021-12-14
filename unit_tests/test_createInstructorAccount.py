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
        self.account1 = createAccount.objects.create( isAdmin = True,isIns = True, isTA = False, createNewAccount= True, createUser = 'JasonRock', createPassword = '123',  generateUserid= '2468')
        self.account2 = createAccount.objects.create( isAdmin = True,isIns = True, isTA = False, createNewAccount= False, createUser = 'JRock', createPassword = 'admin',  generateUserid= '8468')
        self.account3 = createAccount.objects.create(isAdmin=False, isIns = True, isTA = False,createNewAccount= False , createUser='JasonRock',
                                                    createPassword='123', generateUserid='2468')
    def test_falseCreateNewAccount(self):
        self.assertEqual(self.account2.createNewAccount.__bool__(False),  msg= "Acount two cannot be created")

    def test_trueCreateNewAccount(self):
        self.assertEqual(self.account1.createNewAccount.__bool__(True), msg="Acount one can be created")

    def test_adminRequest(self):
        self.assertTrue (self.account1.isAdmin.__bool__(True), msg="admin request passed")

    def test_notAdminRequest(self):
        self.assertFalse(self.account2.isAdmin.__bool__(False), msg="admin request failed")

    def test_accountCreated(self):
        self.assertTrue(self.account1.isAdmin.__bool__(True), msg="admin request passed")
        self.assertTrue(self.account1.createNewAccount.__bool__(True), msg="Acount one can be created")

    def test_accountNotCreated(self):
        self.assertFalse(self.account2.isAdmin.__bool__(False), msg="admin request failed")
        self.assertEqual(self.account2.createNewAccount.__bool__(False),  msg= "Acount two cannot be created")
class TestCreateAccount(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.account1 = createAccount.objects.create(isAdmin=True, isIns = True, isTA = False,createNewAccount=True, createUser='JasonRock',
                                                     createPassword='123', generateUserid='2468')
        self.account2 = createAccount.objects.create(isAdmin=True,isIns = True, isTA = False, createNewAccount=True, createUser=' ',
                                                     createPassword='admin', generateUserid='8468')
        self.account3 = createAccount.objects.create(isAdmin=False, isIns =  True, isTA = False,createNewAccount=True, createUser='JasonR',
                                                     createPassword=' ', generateUserid='1234')
        self.account4 = createAccount.objects.create(isAdmin=True, isIns = False, isTA = True, createNewAccount=False, createUser='JasonRock',
                                                     createPassword='123', generateUserid='2468')
        self.account3 = createAccount.objects.create(isAdmin=True, isIns=False, isTA=True, createNewAccount=False,
                                                     createUser='JasonRock',
                                                     createPassword='123', generateUserid='2468')

    def test_getAccountNotTrue(self):
        self.assertEqual(self.account2.createNewAccount.__bool__(False), msg="Acount two cannot be created")
        self.assertFalse(self.account3.isAdmin.__bool__(False), self.account3.createNewAccount.__bool__(False), msg = "Account not true")

    def test_getAccountTrue(self):
        self.assertTrue(self.account1.isAdmin.__bool__(True), msg="admin request passed")
        self.assertTrue(self.account1.createNewAccount.__bool__(True), msg="Acount one can be created")
        self.assertEqual(self.account1.createUser.__eq__("JasonRock"), self.account1.createPassword.__eq__("123"), self.account1.generateUserid.__eq__("2468"))

    def test_createNewAccountTATrue(self):
        self.assertRaises(AssertionError, self.account4.isTa.__bool__(True), msg = "TA account and instructor account cannot b e created at the same time ")

    def test_createNewAccountInstructorTrue(self):
        self.assertEqual(self.account1.isIns.__bool__(True), msg = "created ins account")

    # def test_createNewAccountTAcreateNewAccountInstructorFalse(self):
    #
    #
    # def test_createNewAccountTAcreateNewAccountInstructorTrue(self):
    #     pass

    def test_newInstructorcreated(self):


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