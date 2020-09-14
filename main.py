from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import date
import time
import csv
from Reader import jsonReader
from RequestManager import requestManager
from CaseMonitor import caseMonitor

currentDate = date.today().strftime("%b-%d-%Y")
currentTime = time.strftime("%H:%M:%S", time.localtime())
reportDirPath = "./FailureCases_"+currentDate+"_"+currentTime
reader = jsonReader("./testCases.json")
requester = requestManager("https://www.phptravels.net/register")
monitor = caseMonitor()
report = []
report.append(["ID","FirstName","LastName","Mobile","Email","Password","ConfirmedPassword","ExpectedResult","TestResult","ExpectedReason"])




while True:
    signUpCase = reader.GetSignUpCase()
    if signUpCase == None:
        break
    ExpectedResult = monitor.checkSignUpCase(signUpCase)
    requester.OpenBrowser()
    requester.SignUpRequest(signUpCase)
    TestResult = requester.SaveRequestResults(reportDirPath, signUpCase, ExpectedResult)
    requester.CloseBrowser()
    
    report.append([signUpCase["Test_ID"],signUpCase["FirstName"],signUpCase["LastName"],signUpCase["Mobile"],signUpCase["Email"],signUpCase["Password"],signUpCase["ConfirmPassword"],ExpectedResult,TestResult,signUpCase["Reason"]])

with open('TestReport.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in report:
        csvwriter.writerow(row)



print"##############THE END#################" 
