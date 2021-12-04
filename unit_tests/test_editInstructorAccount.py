from final_project.editInstructorAccount import EditInstructorAccount
from final_project.isAdmin import isAdmin
import unittest
from project_apps.models import Users
from django.test import Client

class TestEditInstructorAccount(unittest.TestCase):
    def setUp(self):
        self.TAUser = Users.objects.create(userName='TA1', password='YayTA', firstName='First', lastName='Last',
                                           email='ottmakai000@gmail.com', group='TA', userID=3)
        self.InstructorUser = Users.objects.create(userName='Instructor1', password='YayInstructor', firstName='First',
                                                   lastName='Last', email='krottman@uwm.edu', group='Instructor', userID=2)
        self.AdministratorUser = Users.objects.create(userName='Admin1', password='YayAdmin', firstName='First',
                                                      lastName='Last', email='littleotterocean@gmail.com',
                                                      group="Administrator", userID=1)

    def test_isAdminFalseTA(self):
        self.assertEqual(False, isAdmin.adminPermission(self.TAUser.group),
                         msg= "test_editInstructorAccount.test_isAdminFalseTA: "
                              "isAdmin returns TA User as admin")

    def test_isAdminFalseInstructor(self):
        self.assertEqual(False, isAdmin.adminPermission(self.InstructorUser.group),
                         msg= "test_editInstructorAccount.test_isAdminFalseInstructor: "
                              "isAdmin returns Instructor User as admin")

    def test_isAdminTrue(self):
        self.assertEqual(True, isAdmin.adminPermission(self.AdministratorUser.group),
                         msg= "test_editInstructorAccount.test_isAdminTrue: "
                              "isAdmin returns Admin User as not admin")

    def test_rightUserID(self):
        #check if user is trying to edit own account, check if is allowed
        self.assertEqual(3, self.TAUser.userID,
                         msg= "test_editInstructorAccount.test_rightUserID: "
                              "userID is not properly matched")

    def test_editAccount(self):
        #need to create format for returning user information, possibly comma separated
            #maybe 'firstname'.'lastname'.'email'
            #should not be able to change username, password, group, and ID
        self.assertEqual("First.Last.ottmakai000@gmail.com", EditInstructorAccount.editAccount(1, "Administrator"),
                         msg= "test_editInstructorAccount.test_editAccount: " 
                              "editAccount does not return the proper concatenation of User information")

