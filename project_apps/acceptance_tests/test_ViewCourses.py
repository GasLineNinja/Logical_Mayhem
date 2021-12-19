from django.contrib.auth.models import User
from django.test import TestCase, Client
from project_apps.models import Users, Courses

class viewCoursesSucess(TestCase):
        def setUp(self):
            self.client = Client()
            self.user1 = Users.object.create(userName = '')
            self.course1 = Courses.objects.create(courseName='CS361', courseNum='1', courseTime = "3", courseDay = "Mon", instructorName = "Jason", taName = 'Aproov', viewC = 'true')


       def test_courseViewed(self):
           response = self.client.post('homepage.html', {'viewCourse' : 'true'})  # if correct username and password
           self.assertEqual(response.url, 'viewCourses.html',[self.course1.courseName, self.course1.courseNum, self.course1.courseTime, self.course1.courseDay, self.course1.instructorName, self.course1.taName],  msg = 'the course is accurate')

       def test_coursesNotViewd(self):
           response = self.client.post('homepage.html', {'viewCourse' : 'false' })
           self.assertEqual(response.url, 'viewCourses.html',[], msg = 'cannot access view courses')


