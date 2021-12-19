from project_apps.models import Users, Courses, Labs
from .User import User
from classes.User import User
from abc import ABC, abstractmethod


class TA(User, ABC):

    def __init__(self, userName, password1, firstName, lastName, phoneNum, email, group="TA"):
        self.username = userName
        self.password = password1
        self.firstname = firstName
        self.lastname = lastName
        self.phonenum = phoneNum
        self.email = email
        self.group = group

    @abstractmethod
    def view_course_assignments(self, username, coursenumber, labnumber):
        list_labs = list(Labs.objects.filter(courseNum=coursenumber, labNum=labnumber,
                                             userName=username))
        return list_labs

    @abstractmethod
    def view_users(self, groupAdmin, groupInstruct, groupTA):
        list_admin = list(Users.objects.filter(group=groupAdmin))
        list_instructors = list(Users.objects.filter(group=groupInstruct))
        list_ta = list(Users.objects.filter(group=groupTA))

        return list_admin + list_instructors + list_ta
