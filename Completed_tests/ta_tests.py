import unittest
from project_apps.models import Users
from classes.ta import TA

class TestTA(unittest.TestCase):
    def setup(self):
        self.TAUser = Users.objects.create(userName='werraj678', password='11111', firstName='Josh',
                                                   lastName='Werra', email='werra@uwmm.edu', group='TA',
                                                   userID=1)
    def test_createBadTA(self):
        with self.assertRaises(BaseException, msg='Does not raise error on incorrect constructor'):
            TA.__init__()