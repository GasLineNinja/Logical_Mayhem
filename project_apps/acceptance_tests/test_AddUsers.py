from django.test import TestCase
from project_apps.models import Users

#test for if preconditions aren't met, test if they are
#test if conditions are given something they aren't expecting
#look for holes

class TestAddUsers(TestCase):
    def test_existingUser(self):
        self.assertEqual(self.existingUser, Users.objects.get(username='ottmakai000'),
                         msg="TestAddUsers:test_existingUser Existing user not found in database")

    def test_badPassword(self):
        with self.assertRaises(ValueError, msg="TestAddUsers:test_badPassword Password input does not match password in database"):
            Users.objects.get(password='badpassword')

    def test_goodPassword(self):
        self.assertEqual(self.existingUser, Users.objects.get(password1='pass1'),
                         msg='TestAddUsers:test_goodPassword ')

    def test_newUserAdmin(self):
        self.assertEqual(self.AdminUser, Users.objects.get(group='Administrator'),
                         msg='TestAddUsers:test_newUserAdmin ')

    def test_newUserInstructor(self):
        self.assertEqual(self.InstructUser, Users.objects.get(group='Instructor'))

    def test_newUserTA(self):
        self.assertEqual(self.TAUser, Users.objects.get(group='TA'))
