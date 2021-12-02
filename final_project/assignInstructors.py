from assignInstructorstoCourses import AssignInstructorsToCoursesInterface


class AdminAssignInstructors(object, AssignInstructorsToCoursesInterface):
    def __init__(self, assignInstructor, instructorName, courseName):
        self.courseName = courseName
        self.instructorName = instructorName
        self.assignInstructor = assignInstructor

    def __str__(self):
        pass

    def assignInstructor(self, InstructorName):
        pass

    def setInstructor(self, courseName, taName):
        pass
