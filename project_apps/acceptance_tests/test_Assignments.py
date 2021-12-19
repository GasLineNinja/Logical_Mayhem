from unittest import TestCase

from django.test import Client
from project_apps.models import Users, Courses, CourseAssign


class test_init(TestCase):

    def setUp(self):
        self.assign2 = Courses.objects.create(assignment='TFS', assignment1='Socket')

    def test_viewCourseSelected(self):
        response = self.client.post('/', {'coursename' : 'CompSci 361 Intro to Software Engineering'})  # if correct username and password
        #positive test case that should run smoothly if the code is correct
        response = self.client.post('/', {
            'coursename': 'CompSci 361 Intro to Software Engineering'})  # if correct username and password
        self.assertEqual(response.url, '/assignments/')

        response = self.client.get('/assignments/', {'name': self.client.courses})
        self.assertEqual((response.context['assignments'], [self.assign.assignment,self.assign.assignment1 ]),  msg = 'assignlist');  # assert that we should be in things page

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
        self.assertEqual(response.url, '/home/', msg = "assignments not viewed")
        self.assertEqual(response.url, '/home/', msg="Error : assignments not viewed")


class test_viewAssignments(TestCase):
    def setUp(self):
        self.client = Client()
        self.course = Courses.objects.create(courseName='CompSci 361 Intro to Software Engineering', courseTime='MW 10:00a')
        self.assign = Courses.objects.create(assignment = 'TDD', assignment1 = 'AC Test')
        self.course = Courses.objects.create(courseName='CompSci 361 Intro to Software Engineering',
                                             courseTime='MW 10:00a')
        self.assign = Courses.objects.create(assignment='TDD', assignment1='AC Test')

        self.course2 = Courses.objects.create(courseName='CompSci 337 Systems Programming')
        self.assign2 = Courses.objects.create(assignment='TFS', assignment1='Socket')

        self.course3 = Courses.objects.create(courseName='CompSci 351')


    def test_noAssignmentsExists(self):
        #if tthere are no assignmetns in the list we will still display empty assignment page
        response = self.client.post('/', {
           'courseName': 'CompSci 361 Intro to Software Engineering'})  # if correct username and password
            'courseName': 'CompSci 351'})  # if correct username and password
        self.assertEqual(response.url, '/assignments/')

        response = self.client.get('/assignments/', {'name': self.client.courses})
        self.assertEqual((response.context['assignments'], [self.assign.assignment, self.assign.assignment1]),
                             msg='assignlist');  # assert th
        self.assertEqual((response.context['assignments'], []),
                         msg= ' No assignments exist')

    def test_assignmentsViewed(self):
         #wrong assignments viewed
        response = self.client.post('/', {
            'coursename': 'CompSci 361 Intro to Software Engineering'})  # if correct username and password
        self.assertEqual(response.url, '/assignments/')
@@ -63,25 +71,27 @@ def test_assignmentsViewed(self):
        self.assertEqual((response.context['assignments'], ["TFS", "Socket"]),
                         msg='WRONG ASSIGNMENTS');  # assert that we should be in things page



    def test_assignmentsMissing(self):
        #one or more assignments not displayed
        response = self.client.post('/', {
            'coursename': 'CompSci 337 Systems Programming'})  # if correct username and password
        self.assertEqual(response.url, '/assignments/')

        response = self.client.get('/assignments/', {'name': self.client.courses})
        self.assertEqual((response.context['assignments'], [ ]),  msg='No assignments Created');  # assert that we should be in things page

        self.assertEqual((response.context['assignments'], []),
                         msg='No assignments Created');  # assert that we should be in things page

    def test_wrongAssignment(self):
        #course and assignments do not match
        response = self.client.post('/', {
            'coursename': 'CompSci 337 Systems Programming'})  # if correct username and password
        self.assertEqual(response.url, '/assignments/')

        response = self.client.get('/assignments/', {'name': self.client.courses})
        self.assertEqual((response.context['assignments'], [ "TDD", self.assign.assignment1]),
        self.assertEqual((response.context['assignments'], ["TDD", self.assign.assignment1]),
                         msg='wrongassignmnets');  # assert that we should be in things page
