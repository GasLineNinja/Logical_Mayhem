from django.db import models
# Create your models here.


class Users(models.Model):
    userName = models.CharField(max_length=25)
    password1 = models.CharField(max_length=25)
    password2 = models.CharField(max_length=25)
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    phoneNum = models.CharField(max_length=15, default=0)
    email = models.CharField(max_length=50)
    group = models.CharField(max_length=25)


class Courses(models.Model):
    courseName = models.CharField(max_length=100)
    courseNum = models.CharField(max_length=4, default=0000)
    courseTime = models.TimeField()
    courseDay = models.CharField(max_length=15, default=None)
    instructorName = models.CharField(max_length=50)
    taName = models.CharField(max_length=50)


class Labs(models.Model):
    courseName = models.CharField(max_length=100)
    labNum = models.IntegerField()
    labTime = models.CharField(max_length=50)
    taName = models.CharField(max_length=50)


class CourseAssign(models.Model):
    courseName = models.CharField(max_length=100)
    assignmentNum = models.IntegerField()
    assignment = models.CharField(max_length=50)
    assignment1 = models.CharField(max_length=50)


class createAccount(models.Model):
    createNewAccount = models.CharField(max_length=100)
    createUser = models.IntegerField()
    createPassword = models.CharField(max_length=50)
    generateID = models.CharField(max_length=50)