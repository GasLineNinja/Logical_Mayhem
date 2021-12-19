import unittest
from project_apps.models import Users
from classes.Instructor import Instructor

class TestInstructor(unittest.TestCase):

    def setup(self):
        self.InstructorUser = Users.objects.create(userName='boettc74', password='11111', firstName='Danny',
                                                   lastName='Boettcher', email='boettc74@uwmm.edu', group='Instructor',
                                                   userID=2)

    def test_createBadInstructor(self):
        with self.assertRaises(BaseException, msg='Does not raise error on incorrect constructor'):
            Instructor.__init__()

    def test_noRealUser(self):
        self.assertEquals(False,Instructor.check_for_existing_user(self,"NotARealPerson","John","Doe"),msg="Does not return falseon fake user")

    def test_realUser(self):
        self.assertEquals(False,Instructor.check_for_existing_user(self,"boettc74","Danny","Boettcher"),msg="Does not return true on real user")

    def test_wrongParameters(self):
        self.assertEquals(False,Instructor.check_for_existing_user(self,"boettc74","Danny",123453234),msg="Does not return false on numerical parameter")

    def test_shortParameters(self):
        with self.assertRaises(BaseException,msg="Does not throw exception on two paramters"):
            self.assertEquals(False,Instructor.check_for_existing_user(self,"boettc74","Danny"))

    def test_longParameters(self):
        with self.assertRaises(BaseException,msg="Does not throw exception on four paramters"):
            self.assertEquals(False,Instructor.check_for_existing_user(self,"boettc74","Danny","Boettcher","boettc74@uwm.edu"))

    def test_viewStringNumbers(self):
        with self.assertRaises(BaseException,msg="Does not throw error on string parameter"):
            Instructor.view_course_assignments(self,"Billy","1234",543)

    def test_viewShortParameters(self):
        with self.assertRaises(BaseException,msg="Does not throw error on two parameters"):
            Instructor.view_course_assignments(self,"Billy",543)

    def test_viewStringNumbers(self):
        with self.assertRaises(BaseException,msg="Does not throw error on four parameters"):
            Instructor.view_course_assignments(self,"Billy",194,373,543)

    def test_assignBadCourse(self):
        with self.assertRaises(BaseException,msg='Does not raise error on numerical inputs'):
            Instructor.assign_courses(self,143,225,543,869)