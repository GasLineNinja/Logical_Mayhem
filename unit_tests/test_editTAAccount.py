import unittest
from project_apps.models import Users
from final_project.editTAAccount import EditTAAccount
from final_project.isAdmin import isAdmin
from django.test import Client

class TestEditTAAccount(unittest.TestCase):
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
                         msg="test_editTAAccount.test_isAdminFalseTA: "
                             "isAdmin returns TA User as admin")

    def test_isAdminTrue(self):
        self.assertEqual(True, isAdmin.adminPermission(self.AdministratorUser.group),
                         msg= "test_editTAAccount.test_isAdminTrue: "
                              "isAdmin returns Admin User as not admin")

    def test_rightUserID(self):
        #check if user is trying to edit own account, check if is allowed
        self.assertEqual(3, self.TAUser.userID,
                         msg= "test_editTAAccount.test_rightUserID: "
                              "userID is not properly matched")

    def test_editAccount(self):
        #need to create format for returning user information, possibly comma separated
            #maybe 'firstname'.'lastname'.'email'
            #should not be able to change username, password, group, and ID
        self.assertEqual("First.Last.ottmakai000@gmail.com", EditTAAccount.editAccount(3, "Administrator"),
                         msg= "test_editTAAccount.test_editAccount: " 
                              "editAccount does not return the proper concatenation of User information")

