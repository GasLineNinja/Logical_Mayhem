from django.test import TestCase
from project_apps.models import Users

#test for if preconditions aren't met, test if they are
#test if conditions are given something they aren't expecting
#look for holes

class TestAddUsers(TestCase):
    def setUp(self):
        self.existingUser = Users.objects.create(userName="ottmakai000", password1="pass1")
        self.AdminUser = Users.objects.create(group='Administrator')
        self.InstructUser = Users.objects.create(group='Instructor')
        self.TAUser = Users.objects.create(group='TA')

    def test_findAdmin(self):
        self.assertEqual(self.AdminUser, Users.objects.get(group='Administrator'),
                            msg='TestAddUsers:test_findAdmin Admin user does not exist in database')

    def test_uniqueUsername(self):
        self.assertEqual(self.existingUser, Users.objects.get(username='ottmakai000'),
                         msg='TestAddUsers:test_uniqueUsername Existing user not found in database')

    def test_existingUsername(self):
        pass

    def test_noUsername(self):
        pass

    def test_addPassword(self):
        pass

    def test_noPassword(self):
        pass

    def test_addFirstName(self):
        pass

    def test_noFirstName(self):
        pass

    def test_addLastName(self):
        pass

    def test_noLastName(self):
        pass

    def test_addPhoneNum(self):
        pass

    def test_noPhoneNum(self):
        pass

    def test_addGroup(self):
        pass

    def test_noGroup(self):
        pass
