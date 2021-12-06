from assignInstructorstoCourses import AssignInstructorsToCoursesInterface


class AdminAssignInstructors(object):
    def __init__(self, assignInstructor, instructorName, courseName):
        self.courseName = courseName
        self.instructorName = instructorName
        self.assignInstructor = assignInstructor

    def assignInstructor(self, InstructorName):
        #Precondition: isAdmin must be true and an admin must be logged in
        #Postcondition: an instructor can now be assigned to a course
        pass

    def setInstructor(self, courseName, instructorName):
        #Precondition: courseName must be a course that is already created
        #Precondition: instructorName must be an instructor with a created account
        #Postcondition: the Instructor is now added to the course
        pass
