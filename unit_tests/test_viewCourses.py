from django.test import TestCase
from django.test import Client
from project_apps.models import Users, Courses, Labs

class test_viewCourses(TestCase):
    def setup(self):
        self.client = Client();

        self.user1 = Users.objects.create(userName='mdstrand', group='administrator')
        self.user2 = Users.objects.create(userName='sghost', group='Instructor')
        self.user3 = Users.objects.create(userName='hbirdman', group='TA')

        self.course1 = Courses.objects.create(courseName='CompSci 337 Systems Programming')
        self.course2 = Courses.objects.create(courseName='CompSci 361 Intro to Software Engineering')
        self.course3 = Courses.objects.create(courseName='INFOST 695 Ethical Hacking 1')

    def viewCoursesAdmin(self):
        response = self.user1.post('/', {'First name:', 'Space', 'Last name:', 'Ghost'})
        self.assertEquals(response.url, "/courseInfo/")

        response = self.user1.post('/', {'First name:', 'Harvey', 'Last name:', 'Birdman'})
        self.assertEquals(response.url, "/courseInfo/")

    def viewCoursesInstructor(self):
        response = self.user2.post('/', {'First name:', 'Michael', 'Last name:', 'Strand'})
        self.assertEqual(response.context['message'], 'There are no courses assigned')

        response = self.user2.post('/', {'First name:', 'Harvey', 'Last name:', 'Birdman'})
        self.assertEquals(response.url, "/courseInfo/")

    def viewCoursesTa(self):
        response = self.user2.post('/', {'First name:', 'Michael', 'Last name:', 'Strand'})
        self.assertEqual(response.context['message'], 'There are no courses assigned')

        response = self.user2.post('/', {'First name:', 'Space', 'Last name:', 'Ghost'})
        self.assertEquals(response.url, "/courseInfo/")

