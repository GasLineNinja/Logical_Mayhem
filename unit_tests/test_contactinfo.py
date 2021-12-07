import unittest
from project_apps.models import Users
from django.test import Client
from final_project import editContactInfo

class test_ContactInfo(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.TAUser = Users.objects.create(userName='Dan', password='YayTA', firstName='First', lastName='Last',
                                           email='boettc74@uwm.edu', group='TA', userID=3)
        self.InstructorUser = Users.objects.create(userName='Instructor1', password='YayInstructor', firstName='First',
                                                   lastName='Last', email='krottman@uwm.edu', group='Instructor',
                                                   userID=2)


    def test_validEmail(self):
        self.assertEquals(True, editContactInfo.editInfo("boettc75@uwm.edu"))

    def test_numEmail(self):
        self.assertEquals(False, editContactInfo.editInfo(1234564324567))

    def test_longEmail(self):
        self.assertEquals(False, editContactInfo.editInfo("boettcbhdaiugsjbfsbufseugyfe75@uwm.edu"))

    def test_editInstructorPermissions(self):
        response = self.user2.post('/', {'First name:', 'Instructor1', 'Last name:', 'YayInstructor'})
        self.assertEqual(response.url, '/editInfo/')

    def test_editTAPermissions(self):
        response = self.user2.post('/', {'First name:', 'Dan', 'Last name:', 'YayTA'})
        self.assertEqual(response.url, '/editInfo/')