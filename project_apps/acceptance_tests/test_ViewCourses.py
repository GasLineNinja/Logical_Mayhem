from django.contrib.auth.models import User
from django.test import TestCase, Client
from project_apps.models import Users, Courses

class viewCoursesSucess(TestCase):
        def setUp(self):
            self.client = Client()
            self.course = Courses.objects.create(courseName='CS361', coursesNum='1', instructorName="Jason",
                                                 viewC='true')

        def test_courseViewed(self):
            response = self.client.post('homepage.html', {'viewCourse': 'true'})
            self.assertEqual(response.url, 'viewCourses', [self.course.courseName, self.course.courseNum, self.course.instructorName, self.course.viewC])

        def test_coursesNotViewd(self):
            response = self.client.post('homepage.html', {'viewCourse': 'false'})
            self.assertEqual(response.url, 'viewCourses.html', [], msg='cannot access view courses')
