from django.db import models
# Create your models here.


class Users(models.Model):
    userName = models.CharField(max_length=25)
    password1 = models.CharField(max_length=25)
    password2 = models.CharField(max_length=25)
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    group = models.CharField(max_length=25)


class Courses(models.Model):
    courseName = models.CharField(max_length=100)
    courseNum = models.CharField(max_length=4, default=0000)
    courseTime = models.TimeField()
    courseDay = models.CharField(max_length=15, default=None)
    instructorName = models.CharField(max_length=50)
    taName = models.CharField(max_length=50)
    
class ContactPhone(models.Model):
    phoneNum = models.intField(max_length=10)

    def __init__(self, num):
        self.phoneNum = num

    def set(self, num):
        self.phoneNum = num

    def get(self):
        return self.phoneNum
class ContactEmail(models.Model):
    email = models.CharField(max_length=25)

    def __init__(self, email):
        self.email = email

    def set(self, email):
        self.email = email

    def get(self):
        return self.email


class Labs(models.Model):
    courseName = models.CharField(max_length=100)
    labNum = models.IntegerField()
    labTime = models.CharField(max_length=50)
    taName = models.CharField(max_length=50)


