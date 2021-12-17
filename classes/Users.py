from abc import ABC, abstractmethod


class User(ABC):

    @abstractmethod
    def set_username(self, username):
        pass

    def set_password(self, password1):
        pass

    def set_first_name(self, firstname):
        pass

    def set_last_name(self, lastname):
        pass

    def set_phone_num(self, phonenum):
        pass

    def set_email(self, email):
        pass

    def view_users(self, group1, group2, group3):
        pass

    def assign_courses(self, coursenumber, labnumber, firstname, lastname):
        pass

    def view_course_assignments(self, username, coursename, labnumber):
        pass

    def check_for_existing_user(self, username, firstname, lastname):
        pass

    def check_for_existing_course(self, coursenumber):
        pass

    def check_for_existing_lab(self, coursename, labnumber):
        pass