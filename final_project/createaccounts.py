from abc import ABC, abstractmethod


class CreateAccountsInterface(ABC):
    @abstractmethod
    def getAccount(createNewAccount):
        pass

    @abstractmethod
    def createAccount(createNewAccountTA, createNewAccountInstructor, createUser, createPassword):
        pass

    @abstractmethod
    def saveAccount(generateUserID):
        pass



