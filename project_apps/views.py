from django.shortcuts import render, redirect
from django.views import View
from .models import Users

# Create your views here.

class Sign_up(View):
    def get(self,request)
        return render(request, ":C/users/mstra/PycharmProjects/Logical_Mayhem/final_project/templates/signup.html",{})
