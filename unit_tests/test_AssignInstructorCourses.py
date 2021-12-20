import unittest

from project.final_project.assignInstructors import AdminAssignInstructors


class TestInitSuite(unittest.TestCase):

    def setUpInit(self):
        self.default = AdminAssignInstructors("true", "Jayson Rock", "Intro to Software Engineering")
        self.different = AdminAssignInstructors("true", "Joey", "System Programming")

    def test_validInstructorName(self):
        self.assertEqual(self.default.instructorName, "Jayson Rock", msg="this is a valid instructor name to assign")

    def test_inValidInstructorName(self):
        self.assertEqual(self.default.instructorName, "Joe", msg="ERROR: this is an invalid instructor name to assign")

    def test_validGroup(self):
        self.assertEqual(self.default.assignInstructor(), "true", msg="admins can assign Instructors to courses")

    def test_invalidGroupTA(self):
        self.assertEqual(self.default.assignInstructor(), "false",
                         msg="ERROR: Only admins can assign Instructors to courses")

    def test_invalidGroupInstructor(self):
        self.assertEqual(self.default.assignInstructor(), "false",
                         msg="ERROR: Only admins can assign Instructors to courses")

    def test_validCourseName(self):
        self.assertEqual(self.default.courseName, "Intro to Software Engineering",
                         msg="the instructor has been assigned to the correct course")

    def test_inValidCourseName(self):
        self.assertEqual(self.default.courseName, "System Programming",
                         msg="ERROR: this course has a different instructor assigned")
