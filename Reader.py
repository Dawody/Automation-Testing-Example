import json

class jsonReader:
    """
    This class is responsible for reading test cases from testCases.json file
    """
    SignUpCasesCounter=0
    def __init__(self, filePath):
        jsonFile = open(filePath, "r")
        jsonReader.data = json.load(jsonFile)
        jsonFile.close()
        print("Test cases had been loaded successfully")

    def GetSignUpCase(self):
        cnt = jsonReader.SignUpCasesCounter
        jsonReader.SignUpCasesCounter = cnt + 1
        if cnt >= len(jsonReader.data["SIGNUP_TEST"]):
            return None
        print">>>  SignUp Case Number = ", (cnt+1)," <<<"
        print"FirstName       : ", jsonReader.data["SIGNUP_TEST"][cnt]["FirstName"]
        print"LastName        : ", jsonReader.data["SIGNUP_TEST"][cnt]["LastName"]
        print"Mobile          : ", jsonReader.data["SIGNUP_TEST"][cnt]["Mobile"]
        print"Email           : ", jsonReader.data["SIGNUP_TEST"][cnt]["Email"]
        print"Password        : ", jsonReader.data["SIGNUP_TEST"][cnt]["Password"]
        print"ConfirmPassword : ", jsonReader.data["SIGNUP_TEST"][cnt]["ConfirmPassword"]
        print"......................................"
        return jsonReader.data["SIGNUP_TEST"][cnt]


