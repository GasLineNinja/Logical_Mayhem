from multiprocessing.connection import Client

from django.test import TestCase
from project_apps.models import Users, Courses


class MyTestCase(TestCase):

    def test_setUp(self):
        self.client = Client()
        self.course = Courses.objects.create(courseName='CS361', coursesNum = '1', instructorName="Jason",  viewC='true')

    def newUserItems(self):
        response = self.client.get('/things/', {'name': self.client.name}) #if admin then
        self.assertEqual(response.context['things'], [], msg='users list')

        response = self.client.post('addCourses', )  # if correct username and password
        self.assertEqual(response.url, '/viewCourses/')  # assert that we should be in things page

    def existingUserItems(self): #if the course already exists
        response = self.client.post('/', {'name': 'bee', 'password': 'honey'})  # if correct username and password
        self.assertEqual(response.url, '/things/')  # assert that we should be in things page

        response = self.client.get('/things/', {'name': self.user.name})
        self.assertEqual(response.context['things'], [self.stuff1.name, self.stuff2.name], msg='users list')

    def newUserWrongItems(self):#invalid items to make a course(view)
        response = self.client.post('/', {'name': 'Jason', 'password': 'Rock'})  # if correct username and password
        self.assertEqual(response.url, '/things/')  # assert that we should be in things page

        response = self.client.get('/things/', {'name': self.client.name})
        self.assertEqual(response.context['things'], [self.stuff1.name, self.stuff2.name], msg='not the users list')

    def existingUserWrongItems(self): #invalid display(view)
        response = self.client.post('/', {''name': 'Jason', 'password': 'Rock''})  # if correct username and password
        self.assertEqual(response.url, '/things/')  # assert that we should be in things page

        response = self.client.get('/things/', {'name': self.user.name})
        self.assertEqual(response.context['things'], [],  msg='not the users list')

    def additems(self): # add items and update to views
        response = self.client.post('/', {'name': 'amy', 'password': 'pass'})  # if correct username and password
        self.assertEqual(response.url, '/things/')  # assert that we should be in things page

        response = self.client.get('/things/', {'stuff': 'glasses'})
        self.assertEqual(response.context['things'],  [self.stuff1.name, self.stuff2.name, 'glasses'],  msg='the users list')

    def additemsNew(self): # additional items shown
        response = self.client.post('/', {'name': 'bee', 'password': 'honey'})  # if correct username and password
        self.assertEqual(response.url, '/things/')  # assert that we should be in things page

        response = self.client.get('/things/', {'stuff': 'pencil'})
        self.assertEqual(response.context['things'], ['pencil'], msg= 'the users list')

    def donotadditems(self): #items that should not be added are added
        response = self.client.post('/', {'name': 'amy', 'password': 'pass'})  # if correct username and password
        self.assertEqual(response.url, '/things/')  # assert that we should be in things page

        response = self.client.get('/things/', {'stuff': ''})
        self.assertEqual(response.context['things'], [self.stuff1.name, self.stuff2.name],
                         msg='dont add empty items')

    def donotadditemsNew(self):
        response = self.client.post('/', {'name': 'bee', 'password': 'honey'})  # if correct username and password
        self.assertEqual(response.url, '/things/')  # assert that we should be in things page

        response = self.client.get('/things/', {'stuff': ''})
        self.assertEqual(response.context['things'], [], msg='dont add empty items')


