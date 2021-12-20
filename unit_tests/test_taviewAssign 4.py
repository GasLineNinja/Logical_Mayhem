from numpy import msg

from final_project import taViewAssign
from django.test import TestCase
from django.test import Client
from project_apps.models import Users, Courses, CourseAssign


# Unit Tests
class unit_tests(TestCase):

    def test_TAview(self):
        self.assertEquals(True,taViewAssign(self,True, "Assignments"))

    def test_TAviewNumbers(self):
        with self.assertRaises(BaseException,msg="Does not raise error on numbers"):
            taViewAssign(self, True, 1234456432)

    def test_TAviewChar(self):
        with self.assertRaises(BaseException,msg="Does not raise error on char"):
            taViewAssign(self, True, 'a')

    def test_TAviewWrongParameters(self):
        with self.assertRaises(BaseException,msg="Does not raise error on wrong number of parameters"):
            taViewAssign(self, True)

    def test_TAviewWrongParameters(self):
        with self.assertRaises(BaseException,msg="Does not raise error on wrong number of parameters"):
            taViewAssign(self)

    def test_TAviewWrongParameters(self):
        with self.assertRaises(BaseException,msg="Does not raise error on wrong number of parameters"):
            taViewAssign()

    def test_TAviewWrongParameters(self):
        with self.assertRaises(BaseException,msg="Does not raise error on wrong number of parameters"):
            taViewAssign(self, True, "Assignments", "Assignments")



#Acceptance Tests
class test_init(TestCase):

    def setUp(self):
        self.client = Client()
        self.course = Courses.objects.create(courseName='CompSci 361 Intro to Software Engineering')
        self.assign = Courses.objects.create(assignment='TDD', assignment1='AC Test')

        self.course2 = Courses.objects.create(courseName='CompSci 337 Systems Programming')
        self.assign2 = Courses.objects.create(assignment='TFS', assignment1='Socket')

    def test_viewCourseSelected(self):
        #positive test case that should run smoothly if the code is correct
        response = self.client.post('/', {
            'coursename': 'CompSci 361 Intro to Software Engineering'})  # if correct username and password
        self.assertEqual(response.url, '/assignments/')

        response = self.client.get('/assignments/', {'name': self.client.courses})
        self.assertEqual((response.context['assignments'], [self.assign.assignment, self.assign.assignment1]),
                         msg='assignlist');  # assert that we should be in things page

    def test_noCourseExists(self):
        #if a non-existant code is entered
        response = self.client.post('/', {
            'coursename': 'CS431 '})  # if correct username and password
        self.assertEqual(response.context['messege'], 'no such course exists')

    def test_assignmentsViewed(self):
            #if not taken to correct page to view assignments fail
        response = self.client.post('/', {
            'coursename': 'CompSci 361 Intro to Software Engineering'})  # if correct username and password
        self.assertEqual(response.url, '/home/', msg="Error : assignments not viewed")


class test_viewAssignments(TestCase):
    def setUp(self):
        self.client = Client()
        self.course = Courses.objects.create(courseName='CompSci 361 Intro to Software Engineering',
                                             courseTime='MW 10:00a')
        self.assign = Courses.objects.create(assignment='TDD', assignment1='AC Test')

        self.course2 = Courses.objects.create(courseName='CompSci 337 Systems Programming')
        self.assign2 = Courses.objects.create(assignment='TFS', assignment1='Socket')

        self.course3 = Courses.objects.create(courseName='CompSci 351')

    def test_noAssignmentsExists(self):
        #if tthere are no assignmetns in the list we will still display empty assignment page
        response = self.client.post('/', {
            'coursename': 'CompSci 351'})  # if correct username and password
        self.assertEqual(response.url, '/assignments/')

        response = self.client.get('/assignments/', {'name': self.client.courses})
        self.assertEqual((response.context['assignments'], []),
                         msg= ' No assignments exist')

    def test_assignmentsViewed(self):
         #wrong assignments viewed
        response = self.client.post('/', {
            'coursename': 'CompSci 361 Intro to Software Engineering'})  # if correct username and password
        self.assertEqual(response.url, '/assignments/')

        response = self.client.get('/assignments/', {'name': self.client.courses})
        self.assertEqual((response.context['assignments'], ["TFS", "Socket"]),
                         msg='WRONG ASSIGNMENTS');  # assert that we should be in things page

    def test_assignmentsMissing(self):
        #one or more assignments not displayed
        response = self.client.post('/', {
            'coursename': 'CompSci 337 Systems Programming'})  # if correct username and password
        self.assertEqual(response.url, '/assignments/')

        response = self.client.get('/assignments/', {'name': self.client.courses})
        self.assertEqual((response.context['assignments'], []),
                         msg='No assignments Created');  # assert that we should be in things page

    def test_wrongAssignment(self):
        #course and assignments do not match
        response = self.client.post('/', {
            'coursename': 'CompSci 337 Systems Programming'})  # if correct username and password
        self.assertEqual(response.url, '/assignments/')

        response = self.client.get('/assignments/', {'name': self.client.courses})
        self.assertEqual((response.context['assignments'], ["TDD", self.assign.assignment1]),
                         msg='wrongassignmnets');  # assert that we should be in things page






