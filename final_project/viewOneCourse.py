from viewCourses import viewCoursesInterface


class viewAllCourses(object,viewCoursesInterface):
    def __init__(self, viewcourses,course):
        self.viewcourses = viewcourses
        self.course = course

    def view(self, viewcourses, course):
        # Precondition: There are courses in the database
        # Precondition: User chooses one course
        # Post-Condition: User can see the course they have selected
        pass