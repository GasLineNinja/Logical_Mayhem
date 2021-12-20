from abc import ABC, abstractmethod

class AccessDataInterface(ABC):
    @abstractmethod
    def checkAccess(self):
        pass

    @abstractmethod
    def displayAccount(allAcountHolders, allCourses):
        pass