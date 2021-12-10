from abc import ABC, abstractmethod

class EditAccountsInterface(ABC):
    @abstractmethod
    def editAccount(userID):
        pass