from assignTAstoCourses import AssignTAsToCoursesInterface


class AdminAssignInstructors(object, AssignTAsToCoursesInterface):
    def __init__(self, assignInstructor, instructorName, courseName):
        self.courseName = courseName
        self.instructorName = instructorName
        self.assignInstructor = assignInstructor

    def __str__(self):
        pass

    def assignTA(self, TaName):
        pass

    def setTA(self, courseName, taName):
        pass

    def saveTa(self, courseName, taName):
        pass
