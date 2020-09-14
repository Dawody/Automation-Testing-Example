import re




class caseMonitor:
    """ 
    This class can tell if this SignUpTestCase should succeed or fail
    """
    def __init__(self):
        counter = 0
        self.emails_database = set()


    def checkSignUpCase(self, signUpCase):
        Ret = True
        if self.checkName(signUpCase["FirstName"]) == False:
            print"Expected : Failure  (Reason : Invalid First Name)"
            Ret = False
        elif self.checkName(signUpCase["LastName"]) == False:
            print"Expected : Failure (Reason : Invaild Last Name)"
            Ret = False
        elif signUpCase["FirstName"] == signUpCase["LastName"]:
            print"Expected : Failure (Reason : Invalid Names)"
            Ret = False
        elif self.checkMobile(signUpCase["Mobile"]) == False:
            print"Expected : Failure (Reason : Invalid Mobile Number)"
            Ret = False
        elif self.checkEmail(signUpCase["Email"]) == False:
            print"Expected : Failure (Reason : Invalid Email)"
            Ret = False
        elif signUpCase["Email"] in self.emails_database:
            print"Expected : Failure (Reason : Already Signed Email)"
            Ret = False
        elif self.checkPassword(signUpCase["Password"]) == False:
            print"Expected : Failure (Reason : Invalid Password)"
            Ret = False
        elif signUpCase["Password"] != signUpCase["ConfirmPassword"]:
            print"Expected : Failure (Reason : Invalid Confirmed Password)"
            Ret = False 
        else:
            self.emails_database.add(signUpCase["Email"])
            print"Expected : SUCCESS"
        return Ret



    def checkPassword(self, Password):
        """
        check that Password has  @ least 8 chars, 
        @ least one capital letter and @ least one small letter
        """
        if len(Password) < 8:
            return False
        small_flag = capital_flag = False
        for i in Password:
            if i.islower():
                small_flag = True
            elif i.isupper():
                capital_flag = True
        if(small_flag and capital_flag):
            return True
        else:
            return False

    def checkEmail(self, Email):
        """
        check that Email format is ^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$
        """
        emailRegex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(emailRegex,Email)):
            return True
        else:
            return False

    def checkMobile(self, Mobile):
        """
        check that Mobile Number is 11  numbers-only digits and start with 01
        We can also add more acceptable formats like 0112-3456-789
        """
        if ((len(Mobile) != 11) or (Mobile[0]!='0') or (Mobile[1]!='1')):
            return False
        if Mobile.isdigit() :
            return True
        else:
            return False


    def checkName(self, Name):
        """
        check that Name not empty and start with capital letter
        We can also check that Name doesn't contain any numbers or special chars
        """
        if len(Name) == 0:
            return False
        if Name[0].isupper():
            return True
        else:
            return False






