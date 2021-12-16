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

    def test_lessParameters(self):
        with assertRaises(AssertionError, msg= 'TestCreateUser:test_noUsername One too many parameters fails to raise createUser error')
            AddUsers.createUser("", "pass", "fname", "lname", "email", "User", 1234567890)
        pass

    def test_tooManyParameters(self):
        with assertRaises(AssertionError, msg= 'TestCreateUser:test_noUsername No username fails to raise createUser error')
            AddUsers.createUser("", "pass", "fname", "lname", "email", "User", 1234567890, "E Knapp St", 1234567890, "E Knapp St")

    def test_noUsername(self):
        with assertRaises(AssertionError, msg= 'TestCreateUser:test_noUsername No username fails to raise createUser error')
            AddUsers.createUser("", "pass", "fname", "lname", "email", "User", 1234567890, "E Knapp St")

    def test_noPassword(self):
        with assertRaises(AssertionError, msg= 'TestCreateUser:test_noPassword No password fails to raise createUser error')
            AddUsers.createUser("ottmakai000", "", "fname", "lname", "email", "User", 1234567890, "E Knapp St")

    def test_noFirstName(self):
        with assertRaises(AssertionError, msg= 'TestCreateUser:test_noFirstName No first name fails to raise createUser error')
            AddUsers.createUser("ottmakai000", "pass", "", "lname", "email", "User", 1234567890, "E Knapp St")

    def test_noLastName(self):
        with assertRaises(AssertionError, msg= 'TestCreateUser:test_noLastName No last name fails to raise createUser error')
            AddUsers.createUser("ottmakai000", "pass", "fname", "", "email", "User", 1234567890, "E Knapp St")

    def test_noPrivatePhoneNum(self):
        with assertRaises(AssertionError, msg= 'TestCreateUser:test_noPrivatePhoneNum No private phone number fails to raise createUser error')
            AddUsers.createUser("ottmakai000", "pass", "fname", "lname", "email", "User", 0, "E Knapp St")

    def test_noGroup(self):
        with assertRaises(AssertionError, msg= 'TestCreateUser:test_noGroup No group fails to raise createUser error')
            AddUsers.createUser("ottmakai000", "pass", "fname", "lname", "email", "", 1234567890, "E Knapp St")

    def test_noPrivateAddress(self):
        with assertRaises(AssertionError, msg= 'TestCreateUser:test_noPrivataAddress No private address fails to raise createUser error')
            AddUsers.createUser("ottmakai000", "pass", "fname", "lname", "email", "", 1234567890, "")

    def test_noPublicPhoneNum(self):
        with assertRaises(AssertionError, msg= 'TestCreateUser:test_noPublicPhoneNum No public phone number raises createUser error')
            AddUsers.createUser("ottmakai000", "pass", "fname", "lname", "email", "", 1234567890, "E Knapp St", 0)

    def test_noPublicAddress(self):
        with assertRaises(AssertionError, msg= 'TestCreateUser:test_noPublicAddress No public address raises createUser error')
            AddUsers.createUser("ottmakai000", "pass", "fname", "lname", "email", "", 1234567890, "E Knapp St", 0, "")

    def test_createUser(self):
        self.assertEquals(Users.objects.get(userName='ottmakai000'),
                            self.existingUser = AddUsers.createUser("ottmakai000", "pass", "fname", "lname", "email", "User", 1234567890, "E Knapp St"),
                            msg= 'TestCreateUser:test_createUser CreateUser does not successfully return a User')

class TestCheckForExistingUser(TestCase):

    def setUp(self):
       #fix to user Users.objects.create
       self.existingUser = Users.objects.create(userName="ottmakai000", password1="pass", firstName="fname", lastName="lname", email="email", group="User", privatePhoneNum=1234567890, privateAddress="E Knapp St")

"""
    Move tests to isAdmin unit tests

    def test_findAdminTrue(self):
        self.assertTrue(isAdmin.adminPermission('Administrator'),
             msg='TestCreateUser:test_findAdminTrue Admin is not seen as an Admin')

    def test_findAdminFalse(self):
        self.assertFalse(isAdmin.adminPermission('TA'),
             msg='TestCreateUser:test_findAdminFalse TA is seen as an Admin') """

    def test_uniqueUsername(self):
        self.assertFalse(AddUsers.checkForExistingUser('newUser'),
             msg='TestCheckForExistingUser:test_uniqueUsername Unknown user found in database')

    def test_existingUsername(self):
        self.assertTrue(AddUsers.checkForExistingUser('ottmakai000'),
             msg='TestCheckForExistingUser:test_existingUsername Known existent user not found in database')

    def test_noParameter(self):
        with self.assertRaises(AssertionError, msg='TestCheckForExistingUser:test_noParameter Empty parameters pass as sufficient argument'):
            checkForExistingUser()
