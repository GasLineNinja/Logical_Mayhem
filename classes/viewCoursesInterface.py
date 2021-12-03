from abc import ABC, abstractmethod


class ViewCoursesInterface(ABC):
    @abstractmethod
    def viewAssignments(self):
        pass