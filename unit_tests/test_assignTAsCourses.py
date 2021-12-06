import unittest
from project.final_project.assignTAs import AdminAssignTAs


class TestInitSuite(unittest.TestCase):

    def setUpInit(self):
        self.default = AdminAssignTAs("true", "Aproov", "Intro to Software Engineering")
        self.different = AdminAssignTAs("true", "Joey", "System Programming")

    def test_validTAName(self):
        self.assertEqual(self.default.taName, "Aproov", msg="this is a valid TA name to assign")

    def test_inValidTAName(self):
        self.assertEqual(self.default.taName, "Joe", msg="ERROR: this is an invalid TA name to assign")

    def test_validGroup(self):
        self.assertEqual(self.default.assignTa, "true", msg="admins can assign TAs to courses")

    def test_invalidGroupTA(self):
        self.assertEqual(self.default.assignTa, "false",
                         msg="ERROR: Only admins can assign TAs to courses")

    def test_invalidGroupTA(self):
        self.assertEqual(self.default.assignTa, "false",
                         msg="ERROR: Only admins can assign TAs to courses")

    def test_validCourseName(self):
        self.assertEqual(self.default.courseName, "Intro to Software Engineering",
                         msg="the TA has been assigned to the correct course")

    def test_inValidCourseName(self):
        self.assertEqual(self.default.courseName, "System Programming",
                         msg="ERROR: this course has a different TA assigned")
