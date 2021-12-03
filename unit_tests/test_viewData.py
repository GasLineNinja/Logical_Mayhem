from django.test import TestCase
from django.test import Client
from project_apps.models import Users, Courses, Labs


class test_viewData(TestCase):
    def setup(self):
        self.client = Client()
        self.user1 = Users.objects.create(userName='mdstrand', password='12345', firstName='Michael',
                                          lastName='Strand', email='mdstrand@uwm.edu', group='Administrator')
        self.course1 = Courses.objects.create(courseName='CompSci 361 Intro to Software Engineering',
                                              courseTime='MW 10:00a')
        self.lab1 = Labs.objects.create(courseName='CompSci 361 Intro to Software Engineering', labNum='901',
                                        labTime='T 11:00a')

        self.user2 = Users.objects.create(name='sghost', password='12345', firstName='Space', lastName='Ghost',
                                          email='coasttocoast@uwm.edu', group='Instructor')
        self.course2 = Courses.objects.create(courseName='CompSci 337 Systems Programming', courseTime='TTH 10:00a')
        self.lab2 = Labs.objects.create(courseName='CompSci 337 Systems Programming', labNum='801',
                                        labTime='TH 11:00a')

        self.user3 = Users.objects.create(name='hbirdman', password='12345', firstName='Harvey', lastName='Birdman',
                                          email='attorneyatlaw@uwm.edu', group='TA')
        self.course3 = Courses.objects.create(courseName='CompSci 361 Intro to Software Engineering',
                                              courseTime='MW 10:00a')
        self.lab3 = Labs.objects.create(courseName='CompSci 361 Intro to Software Engineering', labNum='902',
                                        labTime='TH 11:00a')

    def viewDataAdmin(self):
        response = self.user1.post('/', {'username:', 'sghost'})
        self.assertEquals(response.url, "/userInfo/")

        response = self.user1.post('/', {'username:', 'hdirdman'})
        self.assertEquals(response.url, "/userInfo/")

    def viewDataInstructors(self):
        response = self.user2.post('/', {'username:', 'hbirdman'})
        self.assertEqual(response.context['message'], "You are not authorized to view content")

        response = self.user2.post('/', {'username:', 'mdstrand'})
        self.assertEqual(response.context['message'], "You are not authorized to view content")

    def viewDataTa(self):
        response = self.user3.post('/', {'username:', 'mdstrand'})
        self.assertEqual(response.context['message'], "You are not authorized to view content")

        response = self.user3.post('/', {'username:', 'sghost'})
        self.assertEqual(response.context['message'], "You are not authorized to view content")
