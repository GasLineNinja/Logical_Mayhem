from createaccounts import CreateAccountsInterface

class CreateInstructorAccount(CreateAccountsInterface):
    def getAccount(createNewAccount):
        #Precondition: the account holder is an admin
        #Precondition: the createNewAccount is true
        #Postcondition: an account will be created
        #createNewAccount: boolean to see if create account was selected by user or not
        pass

    def createAccount(createNewAccountTA, createNewAccountInstructor, createUser, createPassword):
        #Precondition: the getAccount() is true
        #Precondition: user selects either createNewAccountTA or createNewAccountInstructor to be true
        #Postcondition: a new account with instructor permission/login or TA login/permission will be created
        #Postcondition: a new username and password will be generated
        #createUser: stirng to create user name
        #createPassword: string to create a password
        #createnewAcountTA: boolean to make username and password specific for instructor
        #createNEwAccountInstructor: boolean to make sure that TA is false and Instructor is true
        pass

    def saveAccount(generateUserID):
        #Precondition: make sure that username/password are valid
        #Postcondition: match userID to the username and password for the account created for instructors
        #generateUserID: the user account now has an individual ID
        pass