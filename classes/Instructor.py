from project_apps.models import Users, Courses, Labs
from classes.User import User
from abc import ABC, abstractmethod


class Instructor(User,ABC):

    def __init__(self, userName, password1, firstName, lastName, phoneNum, email, group="Instructor"):
        self.username = userName
        self.password = password1
        self.firstname = firstName
        self.lastname = lastName
        self.phonenum = phoneNum
        self.email = email
        self.group = group

    def check_for_existing_user(self, username, firstname, lastname):
        # getting list of users in the database with passed username
        list_users = list(Users.objects.filter(firstName=firstname, lastName=lastname))
        # if len of list for username is less than one user does not exist
        if len(list_users) < 1:
            return False
        return True

    def edit_info(self, username, email, phonenumber, password):
        Users.objects.filter(userName=username).update(email=email, phoneNum=phonenumber, password=password)
        message = f'Your information has been updated'
        return message

    @abstractmethod
    def view_course_assignments(self, username, coursenumber, labnumber):
        list_courses = list(Courses.objects.filter(courseNum=coursenumber, userName=username))
        return list_courses

    @abstractmethod
    def assign_courses(self, coursenumber, labnumber, firstname, lastname):
        if self.check_for_existing_lab(coursenumber, labnumber):
            if self.check_for_existing_user(self, firstname, lastname):
                user_ref = Labs.objects.update(courseNum=coursenumber, labNum=labnumber, taFirstName=firstname,
                                               taLastName=lastname)
                message = f'{user_ref.taFirstName} {user_ref.taLastName} has been added to course' \
                          f'number {user_ref.courseNum}, lab number {user_ref.labNum}'
                return message
            else:
                message = f'Cannot add user to lab. User does not exist'
                return message
        else:
            message = f'Cannot add user to lab. Lab does not exist'
            return message


    @abstractmethod
    def view_users(self, groupAdmin, groupInstruct, groupTA):
        list_admin = list(Users.objects.filter(group=groupAdmin))
        list_instructors = list(Users.objects.filter(group=groupInstruct))
        list_ta = list(Users.objects.filter(group=groupTA))

        return list_admin + list_instructors + list_ta
