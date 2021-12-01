from django.db import models
# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

class Courses(models.Model):
    courseName = models.CharField(max_length=25)

class Labs(models.Model):
    courseName = models.CharField(max_length=25)
    labNum = models.intField(max_length=4)

class ContactPhone(models.Model):
    phoneNum = models.intField(max_length=10)

    def __init__(self):
        return self.phoneNum

class ContactEmail(models.Model):
    email = models.CharField(max_length=25)

    def __init__(self):
        return self.email






