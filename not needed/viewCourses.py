from abc import ABC, abstractmethod

class viewCoursesInterface(ABC):
    @abstractmethod
    def __init__(self, viewCourse, course):
        pass

    @abstractmethod
    def viewCourses(viewCourse, course):
        pass