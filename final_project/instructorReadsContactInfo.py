from readPublicContact import ReadPublicContactInterface

class InstructorReadsContactInfo(object,ReadPublicContactInterface):
    def readPublicContactInfo(viewinfo, information):
        #Precondition: Check if isInstrcutor()
        #Precondition: check if viewInfo is true
        #Postcondition: If true the user wants to see the contact information of all users as a list once they selected the option of viewInfo
        #Side-effects: for the user selected there should be listed in a string format, and can be seen underall data, and admins can see the contact data in alldata access that they have
        #viewInfo: boolean to check if instrcutor wants to view contact information for instruction, a string of assignments that will be printed in appropriate locations for the instrcutor to view
        #information: a string of data that can be printed to show user the contact information of all users
        pass
