from abc import ABC, abstractmethod


class viewAssignmentInterface(ABC):
    @abstractmethod
    def __init__(self, viewCourse, assignments):
        pass


    @abstractmethod
    def viewAssignments(viewCourse, assignments):
        pass

