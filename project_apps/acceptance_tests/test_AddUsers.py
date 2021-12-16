from django.test import TestCase
from project_apps.models import Users

#test for if preconditions aren't met, test if they are
#test if conditions are given something they aren't expecting
#look for holes

class TestAddUsers(TestCase):
    def setUp(self):
        #fix using Users.objects.create
        self.existingUser = Users.objects.create(userName="ottmakai000", password1="pass", firstName="fname", lastName="lname", email="email", group="User", privatePhoneNum=1234567890, privateAddress="E Knapp St")
        self.AdminUser = Users.objects.create(userName="IAmAnAdmin", password1="pass", firstName="fname", lastName="lname", email="email", group="Administrator", privatePhoneNum=1234567890, privateAddress="E Knapp St")
        self.InstructUser = Users.objects.create(userName="IAmAnInstructor", password1="pass", firstName="fname", lastName="lname", email="email", group="Instructor", privatePhoneNum=1234567890, privateAddress="E Knapp St")
        self.TAUser = Users.objects.create(userName="IAmATA", password1="pass", firstName="fname", lastName="lname", email="email", group="TA", privatePhoneNum=1234567890, privateAddress="E Knapp St")

    def test_existingUser(self):
        self.assertEqual(self.existingUser, Users.objects.get(username='ottmakai000'),
                         msg="TestAddUsers:test_existingUser Existing user not found in database")

    def test_badPassword(self):
        with self.assertRaises(AssertionError, msg="TestAddUsers:test_badPassword Password input does not match password in database"):
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
