from abc import ABC, abstractmethod


class AssignTAsToCoursesInterface(ABC):
    def __init__(self, assignTa, TaName, courseName):
        self.TaName = TaName
        self.assignTa = assignTa
        self.courseName = courseName

    @abstractmethod
    def assignTA(self, assignInstructor):
        pass

    @abstractmethod
    def setTa(self, courseName, taName):
        pass

    @abstractmethod
    def saveTa(self, courseName, taName):
        pass
