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
