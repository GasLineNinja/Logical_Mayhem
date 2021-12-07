import unittest
from project_apps.models import Users

class test_ContactInfo(unittest.TestCase):
    def setUp(self):
        self.TAUser = Users.objects.create(userName='Dan', password='YayTA', firstName='First', lastName='Last',
                                           email='boettc74@uwm.edu', group='TA', userID=3)

    def test_validEmail(self):
        self.assertEquals(True, ContactEmail.set(self, "boettc74@uwm.edu"))

    def test_numEmail(self):
        with self.assertRaises(BaseException, msg="Putting a number in email does not give error"):
            ContactEmail.set(self, 123345)

    def test_longEmail(self):
        with self.assertRaises(BaseException, msg="Putting a string over 25 chars in email does not give error"):
            ContactEmail.set(self, "abcdefghijklmnopqrstuvwxyz@uwm.edu")

    def test_validPhone(self):
        self.assertEquals(True, ContactPhone.set(self, 2623333333))

    def test_charPhone(self):
        with self.assertRaises(BaseException, msg="Putting a string in phone number does not give error"):
            ContactPhone.set(self, "Hello")

    def test_longPhone(self):
        with self.assertRaises(BaseException, msg="Putting a int over 10 in phone number does not give error"):
            ContactPhone.set(self, 12345678901234567890)

    def test_shortPhone(self):
        with self.assertRaises(BaseException, msg="Putting a int under 10 in phone number does not give error"):
            ContactPhone.set(self, 12345)
