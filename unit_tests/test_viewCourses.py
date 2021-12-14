from django.shortcuts import render, get_object_or_404
from django.test import TestCase
from django.test import Client

from project_apps.models import Users, Courses, Labs
from final_project import viewCourses, viewAllCourses, viewOneCourse
from django.utils import timezone

class test_viewCourses(TestCase):

    def setup(self):
        self.client = Client()

        #self.user0 = Users.objects.create(userName='purple', password1='purple')
        self.user1 = Users.objects.create(userName='mdstrand', group='administrator')
        self.user2 = Users.objects.create(userName='sghost', group='Instructor')
        self.user3 = Users.objects.create(userName='hbirdman', group='TA')
        self.user0 = Users.objects.create(userName='purple', password1='purple')

        self.course1 = Courses.objects.create(courseName='CompSci 337 Systems Programming')
        self.course2 = Courses.objects.create(courseName='CompSci 361 Intro to Software Engineering')
        self.course3 = Courses.objects.create(courseName='INFOST 695 Ethical Hacking 1')


    #Unit Tests
    def test_allCourses(self):
        self.assertEquals(True,viewAllCourses.view(self, True))

    def test_allCourses(self):
        self.assertEquals(False, viewAllCourses.view(self, False))

    def test_allCoursesWrongParameters(self):
        with self.assertRaises(BaseException,msg="Does not return error on incorrect parameters"):
            viewAllCourses.view(self)

    def test_allCoursesWrongParameters(self):
        with self.assertRaises(BaseException,msg="Does not return error on incorrect parameters"):
            viewAllCourses.view(self, "Hello")

    def test_allCoursesWrongParameters(self):
        with self.assertRaises(BaseException,msg="Does not return error on incorrect parameters"):
            viewAllCourses.view(self,123345)

    def test_allCoursesWrongParameters(self):
        with self.assertRaises(BaseException,msg="Does not return error on incorrect parameters"):
            viewAllCourses.view(self,True,True)

    def test_oneCourse(self):
        self.assertEquals(True,viewOneCourse.view(self,True,"Compsci 361"))

    def test_oneCourseFake(self):
        self.assertEquals(True,viewOneCourse.view(self,True,"Jumping 101"))

    def test_oneCourseFalse(self):
        self.assertEquals(True,viewOneCourse.view(self,False,"Compsci 361"))

    def test_allCoursesWrongParameters(self):
        with self.assertRaises(BaseException,msg="Does not return error on incorrect parameters"):
            viewOneCourse.view(self,True)

    def test_allCoursesWrongParameters(self):
        with self.assertRaises(BaseException,msg="Does not return error on incorrect parameters"):
            viewOneCourse.view(self,True,1234123)

    def test_allCoursesWrongParameters(self):
        with self.assertRaises(BaseException,msg="Does not return error on incorrect parameters"):
            viewOneCourse.view(self,True,False)

    def test_allCoursesWrongParameters(self):
        with self.assertRaises(BaseException,msg="Does not return error on incorrect parameters"):
            viewOneCourse.view(self)

    def test_allCoursesWrongParameters(self):
        with self.assertRaises(BaseException,msg="Does not return error on incorrect parameters"):
            viewOneCourse.view(self,True,"Compsci","Physics")


    #Acceptance Tests
    #def test_noCourses(self, request):
        #response = self.client.post('/', {'userName': 'purple', 'password2': 'purple'})
        #self.assertEqual(response.url, '/homepage/')
        #self.assertEqual(response.url, '/view_courses/')
        #self.assertEqual(response.context['message'], 'No courses have been added yet.')
        #return render(request, "viewCourses.html", {"message": "No courses have been added."})
    
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

    #def test_moreThanOneCourse(self, request):
        #obj = Courses.objects.all()
        #return render(request, 'viewCourses.html', {'obj': obj})