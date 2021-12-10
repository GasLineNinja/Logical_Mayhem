from editaccounts import EditAccountsInterface

class EditInstructorAccount(EditAccountsInterface):
    def editAccount(userID, group):
        #A user can only edit an instructor account if they are an admin (checked with isAdmin)
                #and then that userID is edited
            # or the actual instructor is editing their own account (checked with userID)
        #how is the information being changed?
            #Should we pass things to this function, should it be more based in the html?
        #Precondition: check if isAdmin is true
        #Precondition: enter the right userID
        #Postcondition: the user can make any edits for the account
        #Literally only returning what already exists within the user account
            #We are not editing anything within this function
        #userID: int that acts as an individual's ID for each account
        pass
