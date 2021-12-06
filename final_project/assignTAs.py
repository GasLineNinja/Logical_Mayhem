from assignTAstoCourses import AssignTAsToCoursesInterface


class AdminAssignTAs(object, AssignTAsToCoursesInterface):
    def __init__(self, assignTa, taName, courseName):
        self.courseName = courseName
        self.taName = taName
        self.assignTa = assignTa

    def assignTA(self, TaName):
        # Precondition: isAdmin must be true and an admin must be logged in
        # Postcondition: a TA can now be assigned to a course
        pass

    def setTA(self, courseName, taName):
        # Precondition: courseName must be a course that is already created
        # Precondition: TAName must be a TA with a created account
        # Postcondition: the TA is now added to the course
        pass

