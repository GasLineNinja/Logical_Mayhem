from multiprocessing.connection import Client

from django.test import TestCase
from project_apps.models import Users, Courses


class MyTestCase(TestCase):

    def test_setUp(self):
        self.client = Client()
        self.course = Courses.objects.create(courseName='CS361', coursesNum = '1', instructorName="Jason",  viewC='true')
        self.course2 = Courses.objects.create(courseName='CS377', coursesNum='1', instructorName="Jason", viewC='true')

    def newItems(self):
        response = self.client.get('/homepage/', { 'group': 'Administrator'}) #if admin then add new item
        self.assertEqual(response.context, 'addCourses' , msg='able to add courses')

        response = self.client.post('addCourses', {'Courses.object.create.courseName': 'cs431'} )  # if correct username and password
        self.assertEqual(response.context['addCourses'], [self.course.courseName, self.course2.courseName, self.course3.courseName],  msg='users list')  # assert that we should be in things page

    def existingItems(self): #if the course already exists
        response = self.client.get('/homepage/', {'group': 'Administrator'})  # if admin then
        self.assertEqual(response.context, 'addCourses', msg='able to add courses')

        response = self.client.post('addCourses', {})  # if correct username and password
        self.assertEqual(response.context['addCourses'], [self.course.Coursename, self.course2.name],
                         msg='users list')  # assert that we should be in things page

    def wrongUserInstrucot(self):#invalid items to make a course(view)
        response = self.client.get('/homepage/', {'group': 'Instructor'})  # if admin then
        self.assertEqual(response.context, '/homepage',  'addCourses', msg='able to add courses')

    def wrongUserTA(self):#invalid items to make a course(view)
        response = self.client.get('/homepage/', {'group': 'Ta'})  # if admin then
        self.assertEqual(response.context, '/homepage',  'addCourses', msg='able to add courses')


    def existingUserWrongItems(self): #invalid display(view)
        response = self.client.get('/homepage/', {'group': 'Administrator'})  # if admin then
        self.assertEqual(response.context, 'addCourses', msg='able to add courses')

        response = self.client.post('addCourses', {})  # if correct username and password
        self.assertEqual(response.context['addCourses'], ['class123'],
                         msg='users list')  # assert that we should be in things page

    def addDuplicate(self): # add items and update to views
        response = self.client.get('/homepage/', {'group': 'Administrator'})  # if admin then
        self.assertEqual(response.context, 'addCourses', msg='able to add courses')

        response = self.client.post('addCourses', {'Courses.object.create.courseName': 'cs361'})  # if correct username and password
        self.assertEqual(response.context['addCourses'], ['cs361', self.course2.name],
                         msg='users list')  # assert that we should be in things page

    def missingItems(self): # additional items shown
        response = self.client.get('/homepage/', {'group': 'Administrator'})  # if admin then
        self.assertEqual(response.context, 'addCourses', msg='able to add courses')

        response = self.client.post('addCourses', {})  # if correct username and password
        self.assertEqual(response.context['addCourses'], [self.course.Coursename],
                         msg='users list')  # assert that we should be in things page

    def donotadditems(self): #items that should not be added are added
        response = self.client.get('/homepage/', {'group': 'Administrator'})  # if admin then
        self.assertEqual(response.context, 'addCourses', msg='able to add courses')

        response = self.client.post('addCourses',
                                    {'@*&$N*(^&*SD'})  # if correct username and password
        self.assertEqual(response.context['addCourses'], [self.course.Coursename, self.course2.name],
                         msg='users list')  # assert that we should be in things page

