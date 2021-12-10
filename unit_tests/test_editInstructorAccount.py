import unittest
from project_apps.models import Users
from django.test import Client
import unittest

class TestEditInstructorAccount(unittest.TestCase):
    def setUp(self):
        self.TAUser = Users.objects.create(userName='TA1', password='YayTA', firstName='First', lastName='Last',
                                           email='ottmakai000@gmail.com', group='TA')
        self.InstructorUser = Users.objects.create(userName='Instructor1', password='YayInstructor', firstName='First',
                                                   lastName='Last', email='krottman@uwm.edu', group='Instructor')
        self.AdministratorUser = Users.objects.create(userName='Admin1', password='YayAdmin', firstName='First',
                                                      lastName='Last', email='littleotterocean@gmail.com',
                                                      group="Administrator")

    def test_isAdminFalse(self):
        pass

    def test_isAdminTrue(self):
        pass

    def test_wrongUserID(self):
        pass

    def test_wrongUsername(self):
        pass

    def test_wrongPassword(self):
        pass

    def test_wrongUserIDUsernamePassword(self):
        pass

    def test_rightUserIDUsernamePassword(self):
        pass

    def test_editAccount(self):
        pass