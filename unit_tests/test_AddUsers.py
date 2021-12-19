import unittest
from django.test import TestCase
from project_apps.models import Users
from classes.Administrator import Administrator
from classes.isAdmin import isAdmin
#check if user creates exists, check for existing, and then create user, goes of of preconditions (create user is called) should add a unittests for if there is no username within those parameters
#see if username under username exists,
#test for if preconditions aren't met, test if they are
#test if conditions are given something they aren't expecting
#look for holes

class TestCreateUser(unittest.TestCase):
    def setUp(self):
        pass

    def test_noUsername(self):
        with self.assertRaises(AssertionError, msg= 'TestCreateUser:test_noUsername No username fails to raise '
                                                    'createUser error'):
            Administrator.create_users("", "pass", "fname", "lname", "email", "User", 1234567890)

    def test_noPassword(self):
        with self.assertRaises(AssertionError, msg= 'TestCreateUser:test_noPassword No password fails to raise '
                                                    'createUser error'):
            Administrator.create_users("user", "", "fname", "lname", "email", "User", 1234567890)

    def test_noFirstName(self):
        with self.assertRaises(AssertionError, msg= 'TestCreateUser:test_noFirstName No first name fails to raise '
                                                    'createUser error'):
            Administrator.create_users("user", "pass", "", "lname", "email", "User", 1234567890)

    def test_noLastName(self):
        with self.assertRaises(AssertionError, msg= 'TestCreateUser:test_noLastName No username fails to raise '
                                                    'createUser error'):
            Administrator.create_users("user", "pass", "fname", "", "email", "User", 1234567890)

    def test_noPhoneNum(self):
        with self.assertRaises(AssertionError, msg= 'TestCreateUser:test_noPhoneNum No username fails to raise '
                                                    'createUser error'):
            Administrator.create_users("user", "pass", "fname", "lname", "email", "User", 0)

    def test_noGroup(self):
        with self.assertRaises(AssertionError, msg= 'TestCreateUser:test_noPhoneNum No username fails to raise '
                                                    'createUser error'):
            Administrator.create_users("user", "pass", "fname", "lname", "email", "", 0)

    def test_createUser(self):
        self.assertEquals(Users.objects.get(userName='ottmakai000'))
        self.existingUser = Administrator.create_users("ottmakai000", "pass", "fname", "lname", "email", "User",
                                                       1234567890,
        msg='TestCreateUser:test_createUser CreateUser does not successfully return a User')

class TestCheckForExistingUser(TestCase):

    def setUp(self):
            self.existingUser = Administrator.create_users("ottmakai000", "pass", "fname", "lname", "email", "User",
                                                           1234567890)
            self.AdminUser = Administrator.create_users("admin", "pass", "fname", "lname", "email", "Administrator",
                                                        1234567890)
            self.AdminUser = Administrator.create_users("instruct", "pass", "fname", "lname", "email", "Instructor",
                                                        1234567890)
            self.AdminUser = Administrator.create_users("ta", "pass", "fname", "lname", "email", "TA", 1234567890)

    def test_findAdminTrue(self):
        self.assertTrue(isAdmin.adminPermission('Administrator'),
             msg='TestCreateUser:test_findAdminTrue Admin is not seen as an Admin')

    def test_findAdminFalse(self):
        self.assertFalse(isAdmin.adminPermission('TA'),
             msg='TestCreateUser:test_findAdminFalse TA is seen as an Admin')

    def test_uniqueUsername(self):
        self.assertFalse(Administrator.check_for_existing_user('newUser'),
             msg='TestCreateUser:test_uniqueUsername Unknown user found in database')

    def test_existingUsername(self):
        self.assertTrue(Administrator.check_for_existing_user('ottmakai000'),
             msg='TestCreateUser:test_existingUsername Known existent user not found in database')
