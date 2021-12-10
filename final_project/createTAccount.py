from createaccounts import CreateAccountsInterface


class CreateTAAccount(object, CreateAccountsInterface):
    def __init__(self, createNewAccountTA, createNewAccountInstructor, createUser, createPassword, generateUserId):
        self.generateUserId = generateUserId
        self.createPassword = createPassword
        self.createUser = createUser
        self.createNewAccountInstructor = createNewAccountInstructor
        self.createNewAccountTA = createNewAccountTA

    def getAccount(self, createNewAccount):
        # Precondition: the account holder is an admin
        # Precondition: the createNewAccount is true
        # Postcondition: an account will be created
        # createNewAccount: boolean to see if create account was selected by user or not
        pass

    def createAccount(self, createNewAccountTA, createNewAccountInstructor, createUser, createPassword):
        # Precondition: the getAccount() is true
        # Precondition: user selects either createNewAccountTA or createNewAccountInstructor to be true
        # Postcondition: a new account with instructor permission/login, or ta login/persmission will be created
        # Postcondition: a new username and password will be generated
        # createUser: string to create user name
        # createPassword: string to create password
        # createNewAccountTA: boolean to make username and password specific for TA
        # createNewAccountInstructor: boolean to make sure that Instructor is false and TA is true
        pass

    def saveAccount(self, generateUserID):
        # Precondition: make sure that username/password are valid
        # Postcondition: match generateuserID to the username and password for the account created for TA
        # generateUserID: the user account now has an individual id
        pass
