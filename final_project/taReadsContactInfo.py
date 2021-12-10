from readPublicContact import ReadPublicContactInterface

class TAReadsContactInfo(object,ReadPublicContactInterface):
    def readPublicContactInfo(viewinfo, information):
        #Precondition: Check if isTA()
        #Precondition: check if viewInfo is true
        #Postcondition: If true the user wants to see the contact information of all users as a list once they selected the option of viewInfo
        #Side-effects: for the user selected there should be listed in a string format, and can be seen under all data, and admins can see the contact data in alldata access that they have
        #viewInfo: boolean to check if TA wants to view contact information for instruction, a string of assignments that will be printed in appropriate locations for the TA to view
        #information: a string of data that can be printed to show user the contact information of all users
        pass