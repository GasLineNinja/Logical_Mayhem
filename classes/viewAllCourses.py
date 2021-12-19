from viewCourses import viewCoursesInterface

class viewAllCourses(object,viewCoursesInterface):
    def __init__(self, viewcourses):
        self.viewcourses = viewcourses

    def view (self,viewcourses):
        #Precondition: There are courses in the database
        #Post-Condition: User can see every course in database
        pass