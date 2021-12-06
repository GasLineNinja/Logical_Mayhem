from final_project import createInstructorAccount
from django.test import TestCase
from project_apps.models import Users
from final_project.isAdmin import isAdmin

#test for if preconditions aren't met, test if they are
#test if conditions are given something they aren't expecting
#look for holes

class TestGetAccount(TestCase):
    def setUp(self):
        self.TAUser = Users.objects.create(userName='TA1', password='YayTA', firstName='First', lastName='Last',
                                           email='ottmakai000@gmail.com', group='TA', userID=3)
        self.InstructorUser = Users.objects.create(userName='Instructor1', password='YayInstructor', firstName='First',
                                                   lastName='Last', email='krottman@uwm.edu', group='Instructor',
                                                   userID=2)
        self.AdministratorUser = Users.objects.create(userName='Admin1', password='YayAdmin', firstName='First',
                                                      lastName='Last', email='littleotterocean@gmail.com',
                                                      group="Administrator", userID=1)

    def test_isAdminFalseTA(self):
        self.assertEqual(False, isAdmin.adminPermission(self.TAUser.group),
                         msg= "test_createInstructorAccount.test_isAdminFalseTA: "
                              "isAdmin returns TA User as admin")

    def test_isAdminFalseInstructor(self):
        self.assertEqual(False, isAdmin.adminPermission(self.InstructorUser.group),
                         msg= "test_createInstructorAccount.test_isAdminFalseInstructor: "
                              "isAdmin returns Instructor User as admin")

    def test_isAdminTrue(self):
        self.assertEqual(True, isAdmin.adminPermission(self.AdministratorUser.group),
                         msg= "test_createInstructorAccount.test_isAdminTrue: "
                              "isAdmin returns Admin User as not admin")

    def test_accountCreated(self):
        pass

    def test_accountNotCreated(self):
        pass

class TestCreateAccount(TestCase):
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

class test_SaveAccount(TestCase):
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