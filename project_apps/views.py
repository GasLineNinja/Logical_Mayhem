from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from classes.Administrator import Administrator
from classes.Instructor import Instructor
from classes.ta import TA
from .models import Users, Courses, Labs


# Create your views here.

class SignUp(View):

    # display sing up form
    def get(self, request):
        return render(request, "signup.html", {})

    def post(self, request):
        # get row count of users with Administrator as their group
        rowCount = Users.objects.filter(group='Administrator').count()

        # if no admin
        if rowCount == 0:
            # get passwords to check
            p1 = request.POST['pass1']
            p2 = request.POST['pass2']
            # make sure passwords are the same
            if p1 != p2:
                return render(request, "signup.html", {"message": "Passwords do not match"})
            # if passwords are the same save and redirect to login page
            else:
                # create admin account
                Administrator.create_admin(self, username=request.POST['username'], password=request.POST['pass1'],
                                           group='Administrator')
                return redirect('login')
        # if user exists redirect to login page
        elif Administrator.check_for_existing_user(self, username=request.POST['username']):
            return render(request, "login.html", {"message": "You have an account. Please log in."})
        else:
            # if no user and existing admin account must be created
            return render(request, "login.html", {"message": "You do not have an account. Contact admin to create your "
                                                             "account."})


class Login(View):

    # display login form
    def get(self, request):
        return render(request, "login.html", {})

    # get user input form form
    def post(self, request):
        # check for existing user
        if Administrator.check_for_existing_user(self, username=request.POST['username']):
            u = Users.objects.get(userName=request.POST['username'])
            badPass = (u.password1 != request.POST['pass1'])

            #if user exists and wrong password given
            if badPass:
                return render(request, "login.html", {"message": "bad password"})
            # if user exists but is not administrator
            elif u.group != 'Administrator':
                request.session["username"] = u.userName
                return redirect('userhomepage')
            # if user is administrator
            else:
                request.session["username"] = u.userName
                return redirect('homepage')
        else:
            # user does not exist
            return render(request, "login.html", {"message": "Username not found. Please have the Administrator"
                                                             " create your account."})



class Homepage(View):

    # display homepage
    def get(self, request):
        return render(request, "homepage.html", {})


class UserHomepage(View):

    # display homepage
    def get(self, request):
        return render(request, "userHomepage.html", {})


class AddCourses(View):

    # display add courses page
    def get(self, request):
        return render(request, "addCourses.html", {})

    def post(self, request):
        # check if course exists already
        if Administrator.check_for_existing_course(self, coursenumber=request.POST['coursenum']):
            return render(request, "addCourses.html", {"message": "Course already exists."})
        else:
            # create course if none exists
            Administrator.create_courses(self, coursename=request.POST['coursename'], coursenumber=request.POST['coursenum'],
                                         coursetime=request.POST['coursetime'], courseday=request.POST['courseday'])
            return redirect('addcourses')



class AddUsers(View):

    # display add users page
    def get(self, request):
        return render(request, "addUsers.html", {})

    def post(self, request):
        # check for user in database
        if Administrator.check_for_existing_user(self, username=request.POST['username']):
            return render(request, "addUsers.html", {"message": "User already exists."})
        else:
            # add user if none exists
            Administrator.create_users(self, username=request.POST['username'], firstname=request.POST['fname'],
                                       lastname=request.POST['lname'], email=request.POST['email'],
                                       password=request.POST['pass1'], group=request.POST['group'])

            return redirect('addusers')


class ViewCourses(View):
    # display add users page
    def get(self, request):

        if (Courses.objects.count() == 0):
            return render(request, "viewCourses.html", {"message": "No courses have been added yet."})
        else:
            obj = Courses.objects.all()
            return render(request, 'viewCourses.html', {'obj': obj})


# class ViewCoursesDetails(View):
#    def get(self, request, id):
#        obj = get_object_or_404(Courses, pk=id)
#        return render(request, 'viewCoursesDetails.html', {'obj': obj})


class ViewUsers(View):
    # display add users page
    def get(self, request):
        userobj = Users.objects.all()
        return render(request, 'viewUsers.html', {'userobj': userobj})

def user_detail_page(request, id):
    userobj = get_object_or_404(Users, pk=id)
    return render(request, 'viewUserDetails.html', {'userobj': userobj})


class Assignments(View):

    # display add users page
    def get(self, request):
        return render(request, "assignments.html", {})


def detail_page(request, id):
    obj = get_object_or_404(Courses, pk=id)
    return render(request, 'viewCourseDetails.html', {'obj': obj})
