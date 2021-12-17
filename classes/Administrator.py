from project_apps.models import Users, Courses, Labs
from classes.Users import User
from abc import ABC, abstractmethod


class Administrator(User, ABC):

    def __init__(self, userName, password1, firstName, lastName, phoneNum, email, group="Administrator"):
        self.username = userName
        self.password = password1
        self.firstname = firstName
        self.lastname = lastName
        self.phonenum = phoneNum
        self.email = email
        self.group = group

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_first_name(self, firstname):
        self.firstname = firstname

    def set_last_name(self, lastname):
        self.lastname = lastname

    def set_phone_num(self, phonenum):
        self.phonenum = phonenum

    def set_email(self, email):
        self.email = email

    def check_for_existing_user(self, username):
        # getting list of users in the database with passed username
        list_users = list(Users.objects.filter(userName=username))
        # if len of list for username is less than one user does not exist
        if len(list_users) < 1:
            return False
        return True

    def check_for_existing_course(self, coursenumber):
        # getting list of users in the database with passed username
        list_courses = list(Courses.objects.filter(courseNum=coursenumber))
        # if len of list for username is less than one user does not exist
        if len(list_courses) < 1:
            return False
        return True

    def check_for_existing_lab(self, coursename, labnumber):
        # getting list of users in the database with passed username
        list_labs = list(Labs.objects.filter(courseName=coursename, labNum=labnumber))
        # if len of list for username is less than one user does not exist
        if len(list_labs) < 1:
            return False
        return True

    def create_users(self, username, firstname, lastname, email, password, group):
        # calling method to check for existing user
        if self.check_for_existing_user(username=username):
            message = 'User already exists'
            return message
        user_ref = Users.objects.create(userName=username, group=group, firstName=firstname,
                                        lastName=lastname, password1=password, email=email)
        message = f'User with {user_ref.userName} now created in the system'
        return message

    def create_courses(self, coursename, coursenumber, coursetime, courseday,):
        # calling to check for existing course
        if self.check_for_existing_course(coursenumber):
            message = 'Course already exists'
            return message
        course_ref = Courses.objects.create(courseName=coursename, courseNum=coursenumber, courseTime=coursetime,
                                            courseDay=courseday)
        message = f'Course {course_ref.courseNum} and {course_ref.courseName} has been created'
        return message

    def create_labs(self, coursename, labnumber, labtime):
        # calling to check for existing lab
        if self.check_for_existing_lab(coursename, labnumber):
            message = 'Lab already exists'
            return message
        lab_ref = Labs.objects.create(courseName=coursename, labNum=labnumber, labTime=labtime)
        message = f'Lab number {lab_ref.labNum} for course {lab_ref.courseName} has been created'
        return message

    def assign_courses(self, coursenumber, firstname, lastname):
        # calling to check for existing course
        if self.check_for_existing_course(coursenumber):
            course_ref = Courses.objects.update(courseNum=coursenumber, instructorFirstName=firstname,
                                                instructorLastName=lastname)
            message = f'{course_ref.instructorFirstName} {course_ref.instructorLastName} has been added to course' \
                      f'number {course_ref.courseNum}'
            return message
        else:
            message = 'Cannot add user to course. Course does not exist'
            return message

    def view_users(self, group):
        pass
