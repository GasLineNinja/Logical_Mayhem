from numpy import msg

from final_project import taViewAssign
from django.test import TestCase
from django.test import Client
from project_apps.models import Users, Courses, CourseAssign


class test_init(TestCase):

    def setUp(self):
        self.client = Client()
        self.course = Courses.objects.create(courseName='CompSci 361 Intro to Software Engineering')
        self.assign = Courses.objects.create(assignment='TDD', assignment1='AC Test')

        self.course2 = Courses.objects.create(courseName='CompSci 337 Systems Programming')
        self.assign2 = Courses.objects.create(assignment='TFS', assignment1='Socket')

    def test_viewCourseSelected(self):
        response = self.client.post('/', {
            'coursename': 'CompSci 361 Intro to Software Engineering'})  # if correct username and password
        self.assertEqual(response.url, '/assignments/')

        response = self.client.get('/assignments/', {'name': self.client.courses})
        self.assertEqual((response.context['assignments'], [self.assign.assignment, self.assign.assignment1]),
                         msg='assignlist');  # assert that we should be in things page

    def test_noCourseExists(self):
        response = self.client.post('/', {
            'coursename': 'CS431 '})  # if correct username and password
        self.assertEqual(response.context['messege'], 'no such course exists')

    def test_assignmentsViewed(self):
        response = self.client.post('/', {
            'coursename': 'CompSci 361 Intro to Software Engineering'})  # if correct username and password
        self.assertEqual(response.url, '/home/', msg="assignments not viewed")


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
        response = self.client.post('/', {
            'coursename': 'CompSci 361 Intro to Software Engineering'})  # if correct username and password
        self.assertEqual(response.url, '/assignments/')

        response = self.client.get('/assignments/', {'name': self.client.courses})
        self.assertEqual((response.context['assignments'], [self.assign.assignment, self.assign.assignment1]),
                         msg='assignlist');  # assert th

    def test_assignmentsViewed(self):
        response = self.client.post('/', {
            'coursename': 'CompSci 361 Intro to Software Engineering'})  # if correct username and password
        self.assertEqual(response.url, '/assignments/')

        response = self.client.get('/assignments/', {'name': self.client.courses})
        self.assertEqual((response.context['assignments'], ["TFS", "Socket"]),
                         msg='WRONG ASSIGNMENTS');  # assert that we should be in things page

    def test_assignmentsMissing(self):
        response = self.client.post('/', {
            'coursename': 'CompSci 337 Systems Programming'})  # if correct username and password
        self.assertEqual(response.url, '/assignments/')

        response = self.client.get('/assignments/', {'name': self.client.courses})
        self.assertEqual((response.context['assignments'], []),
                         msg='No assignments Created');  # assert that we should be in things page

    def test_wrongAssignment(self):
        response = self.client.post('/', {
            'coursename': 'CompSci 337 Systems Programming'})  # if correct username and password
        self.assertEqual(response.url, '/assignments/')

        response = self.client.get('/assignments/', {'name': self.client.courses})
        self.assertEqual((response.context['assignments'], ["TDD", self.assign.assignment1]),
                         msg='wrongassignmnets');  # assert that we should be in things page






