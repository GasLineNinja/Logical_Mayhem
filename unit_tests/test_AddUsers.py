from django.test import TestCase
from project_apps.models import Users
from final_project.AddUsers import AddUsers
from final_project.isAdmin import isAdmin

#test for if preconditions aren't met, test if they are
#test if conditions are given something they aren't expecting
#look for holes

class TestCreateUser(TestCase):
    def setUp(self):
        pass

    def test_noUsername(self):
        with assertRaises(AssertionError, msg= 'TestCreateUser:test_noUsername No username fails to raise createUser error')
            AddUsers.createUser("", "pass", "fname", "lname", "email", "User", 1234567890)

    def test_noPassword(self):
        with assertRaises(AssertionError, msg= 'TestCreateUser:test_noPassword No password fails to raise createUser error')
            AddUsers.createUser("user", "", "fname", "lname", "email", "User", 1234567890)

    def test_noFirstName(self):
        with assertRaises(AssertionError, msg= 'TestCreateUser:test_noFirstName No first name fails to raise createUser error')
            AddUsers.createUser("user", "pass", "", "lname", "email", "User", 1234567890)

    def test_noLastName(self):
        with assertRaises(AssertionError, msg= 'TestCreateUser:test_noLastName No username fails to raise createUser error')
            AddUsers.createUser("user", "pass", "fname", "", "email", "User", 1234567890)

    def test_noPhoneNum(self):
        with assertRaises(AssertionError, msg= 'TestCreateUser:test_noPhoneNum No username fails to raise createUser error')
            AddUsers.createUser("user", "pass", "fname", "lname", "email", "User", 0)

    def test_noGroup(self):
        with assertRaises(AssertionError, msg= 'TestCreateUser:test_noPhoneNum No username fails to raise createUser error')
            AddUsers.createUser("user", "pass", "fname", "lname", "email", "", 0)

    def test_createUser(self):
        self.assertEquals(Users.objects.get(userName='ottmakai000'),
                            self.existingUser = AddUsers.createUser("ottmakai000", "pass", "fname", "lname", "email", "User", 1234567890),
                            msg= 'TestCreateUser:test_createUser CreateUser does not successfully return a User')

class TestCheckForExistingUser(TestCase):

    def setUp(self):
            self.existingUser = AddUsers.createUser("ottmakai000", "pass", "fname", "lname", "email", "User", 1234567890)
            self.AdminUser = AddUsers.createUser("admin", "pass", "fname", "lname", "email", "Administrator", 1234567890)
            self.AdminUser = AddUsers.createUser("instruct", "pass", "fname", "lname", "email", "Instructor", 1234567890)
            self.AdminUser = AddUsers.createUser("ta", "pass", "fname", "lname", "email", "TA", 1234567890)

    def test_findAdminTrue(self):
        self.assertTrue(isAdmin.adminPermission('Administrator'),
             msg='TestCreateUser:test_findAdminTrue Admin is not seen as an Admin')

    def test_findAdminFalse(self):
        self.assertFalse(isAdmin.adminPermission('TA'),
             msg='TestCreateUser:test_findAdminFalse TA is seen as an Admin')

    def test_uniqueUsername(self):
        self.assertFalse(AddUsers.checkForExistingUser('newUser'),
             msg='TestCreateUser:test_uniqueUsername Unknown user found in database')

    def test_existingUsername(self):
        self.assertTrue(AddUsers.checkForExistingUser('ottmakai000'),
             msg='TestCreateUser:test_existingUsername Known existent user not found in database')
