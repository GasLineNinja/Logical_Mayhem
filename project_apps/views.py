from django.shortcuts import render, redirect
from django.views import View
from .models import Users, Courses

# Create your views here.

class Sign_up(View):

    # display sing up form
    def get(self, request):
        return render(request, "signup.html",{})

    # get user input form form
    def post(self, request):

        # vaiables for no existing user and bad password
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
            # get new sign up info
            m = Users(userName=request.POST['username'], password1=request.POST['pass1'], password2=request.POST['pass2'])
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
        elif badPassword:
            return render(request, "signup.html", {"message": "bad password"})
        # if user exists redirect to login page
        else:
            request.session["username"] = m.userName
            return redirect('login')

class Login(View):

    # display login form
    def get(self, request):
        return render(request, "login.html", {})

    # get user input form form
    def post(self, request):

        # vaiables for no existing user and bad password
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
            #m = Users.objects.get(userName=request.POST['username'])
            #request.session["username"] = m.userName
            return render(request, "signup.html", {"message": "Username not found. Please create an account."})
        elif badPassword:
            return render(request, "login.html", {"message": "bad password"})
        # if user exists redirect to homepage
        else:
            request.session["username"] = m.userName
            return redirect('homepage')

class Homepage(View):

    # display homepage
    def get(self, request):
        return render(request, "homepage.html", {})

class Add_Courses(View):

    # display add courses page
    def get(self, request):
        return render(request, "addCourses.html", {})

class Add_Users(View):

    # display add users page
    def get(self, request):
        return render(request, "", {})