from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Users, Courses, Labs


# Create your views here.

class SignUp(View):

    # display sing up form
    def get(self, request):
        return render(request, "signup.html", {})

    # get user input form form
    def post(self, request):

        # variables for no existing user and bad password
        noUser = False
        badPassword = False

        # check if user exists
        try:
            m = Users.objects.get(userName=request.POST['username'])
            badPassword = (m.password1 != request.POST['pass1'])
        except:
            noUser = True

        rowCount = Users.objects.filter(group='Administrator').count()

        # if new user
        if rowCount == 0:
            # get new sign up info
            m = Users(userName=request.POST['username'], password1=request.POST['pass1'],
                      password2=request.POST['pass2'], group='Administrator')
            p1 = request.POST['pass1']
            p2 = request.POST['pass2']
            # make sure passwords are the same
            if p1 != p2:
                return render(request, "signup.html", {"message": "Passwords do not match"})
            # if passwords are the same save and redirect to login page
            else:
                m.save()
                request.session["username"] = m.userName
                return redirect('login')
        elif noUser:
            return redirect('login')
        elif badPassword:
            return render(request, "signup.html", {"message": "bad password"})
        # if user exists redirect to login page
        else:
            request.session["username"] = m.userName
            return render(request, "login.html", {"message": "You have an account. Please log in."})


class Login(View):

    # display login form
    def get(self, request):
        return render(request, "login.html", {})

    # get user input form form
    def post(self, request):

        # variables for no existing user and bad password
        noUser = False
        badPassword = False

        # check if user exists
        try:
            m = Users.objects.get(userName=request.POST['username'])
            badPassword = (m.password1 != request.POST['pass1'])
        except:
            noUser = True

        # if new user
        if noUser:
            return render(request, "signup.html", {"message": "Username not found. Please create an account."})
        elif badPassword:
            return render(request, "login.html", {"message": "bad password"})
        # if user exists redirect to homepage
        elif m.group != 'Administrator':
            request.session["username"] = m.userName
            return redirect('userhomepage')
        else:
            request.session["username"] = m.userName
            return redirect('homepage')


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

        noCourse = False

        # checking if course already exists
        try:
            Courses.objects.get(courseName=request.POST['coursename'])
        except:
            noCourse = True

        if noCourse:
            c = Courses(courseName=request.POST['coursename'], courseNum=request.POST['coursenum'],
                        courseDay=request.POST['courseday'], courseTime=request.POST['coursetime'])
            c.save()
            request.session["coursename"] = c.courseName
            return redirect('addcourses')
        else:
            return render(request, "addCourses.html", {"message": "Course already exists."})


class AddUsers(View):

    # display add users page
    def get(self, request):
        return render(request, "addUsers.html", {})

    def post(self, request):

        noUser = False

        try:
            Users.objects.get(userName=request.POST['username'])
        except:
            noUser = True

        if noUser:
            u = Users(userName=request.POST['username'], firstName=request.POST['fname'],
                      lastName=request.POST['lname'], email=request.POST['email'], password1=request.POST['pass1'],
                      group=request.POST['group'])

            u.save()
            request.session["username"] = u.userName
            return redirect('addusers')
        else:
            return render(request, "addUsers.html", {"message": "User already exists"})


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
        return render(request, "", {})


class Assignments(View):

    # display add users page
    def get(self, request):
        return render(request, "assignments.html", {})


def detail_page(request, id):
    obj = get_object_or_404(Courses, pk=id)
    return render(request, 'viewCourseDetails.html', {'obj': obj})
