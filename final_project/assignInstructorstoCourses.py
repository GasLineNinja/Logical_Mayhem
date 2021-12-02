from abc import ABC, abstractmethod


class AssignInstructorsToCoursesInterface(ABC):
    def __init__(self, assignInstructor, instructorName, courseName):
        self.courseName = courseName
        self.instructorName = instructorName
        self.assignInstructor = assignInstructor

    @abstractmethod
    def assignInstructor(assignInstructor):
        pass

    @abstractmethod
    def setInstructor(courseName, taName):
        pass
