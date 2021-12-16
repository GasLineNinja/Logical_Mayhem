from django.test import TestCase
from project_apps.models import Users
from final_project.ViewUsers import checkSelf

class TestCheckSelf(self):
    def setUp(self):

        self.existingUser = Users.objects.create(userName="ottmakai000", password1="pass", firstName="fname", lastName="lname", email="email", group="User", privatePhoneNum=1234567890, privateAddress="E Knapp St")

    def test_notSelf(self):
        self.assertEqual(False, checkSelf('ottmakai000'),
                         msg="TestCheckSelf:test_notSelf not self does not return a false boolean")

     def test_isSelf(self):
        self.assertEqual(True, checkSelf('randomSelf'),
                         msg="TestCheckSelf:test_isSelf self does not return a true boolean")