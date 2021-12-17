from project_apps.models import Users, Courses, Labs
from Users import User


class TA(User):

    def __init__(self, userName, password1, firstName, lastName, phoneNum, email, group="TA"):
        self.username = userName
        self.password = password1
        self.firstname = firstName
        self.lastname = lastName
        self.phonenum = phoneNum
        self.email = email
        self.group = group

    def set_username(self, username):
        self.username = username

    def set_password(self, password1):
        self.password = password1

    def set_first_name(self, firstname):
        self.firstname = firstname

    def set_last_name(self, lastname):
        self.lastname = lastname

    def set_phone_num(self, phonenum):
        self.phonenum = phonenum

    def set_email(self, email):
        self.email = email

    def view_course_assignments(self):
        pass

    def view_users(self):
        pass
