from django.contrib.auth.models import User
from django.test import TestCase, Client
from project_apps.models import Users, Courses



class viewCourses(TestCase):
        def setUp(self):
            self.client = Client()
            # self.user1 = Users.object.create(userName = '')
            # self.course1 = Courses.objects.create(courseName='CS361', courseNum='1', courseTime = "3", courseDay = "Mon", instructorName = "Jason", taName = "Aproov")
            # self.course2 = Courses.objects.create(courseName='CS361', courseNum='1', courseTime = "3", courseDay = "Mon", instructorName = "Jason", taName = "Aproov")

       def test_courseViewed(self):
           response = self.client.post('homepage.html', {'courseName': 'CS361', 'courseNum': '1', 'courseTime' : '3' , 'courseDay' : 'Mon', 'instructorName' : 'Jason', 'taname' : 'Aproov'  })  # if correct username and password
           self.assertEqual(response.url, 'viewCourses.html', msg = 'the course is accurate')  # assert that we should be in things page

       def test_coursesNotViewd(self):
           response = self.client.post('homepage.html', {'courseName': 'CS361', 'courseNum': '1', 'courseTime' : '3' , 'courseDay' : 'Mon', 'instructorName' : 'Jason', 'taname' : 'Aproov'  })
           self.assertEqual(response.url, 'viewCourses.html', msg = 'the course is accurate')

