from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class requestManager:
    """
    This class is resposible for sending requests and receiving the respond
    """
    def __init__(self, URL):
        self.url = URL


    def SignUpRequest(self, signUpCase):
        """
        Send the request
        """
        m_firstName = signUpCase["FirstName"]
        m_secondName = signUpCase["LastName"]
        m_phone = signUpCase["Mobile"]
        m_email = signUpCase["Email"]
        m_password = signUpCase["Password"]
        m_confirmPassword = signUpCase["ConfirmPassword"]
        
        firstName = self.browser.find_element_by_xpath("/html/body/div[2]/div[1]/section/div/div/div[2]/div/form/div[3]/div[1]/div/label/input")
        firstName.send_keys(m_firstName)
        
        secondName = self.browser.find_element_by_xpath("/html/body/div[2]/div[1]/section/div/div/div[2]/div/form/div[3]/div[2]/div/label/input")
        secondName.send_keys(m_secondName)
        
        phone = self.browser.find_element_by_xpath("/html/body/div[2]/div[1]/section/div/div/div[2]/div/form/div[4]/label/input")
        phone.send_keys(m_phone)
        
        email = self.browser.find_element_by_xpath("/html/body/div[2]/div[1]/section/div/div/div[2]/div/form/div[5]/label/input")
        email.send_keys(m_email)
        
        password = self.browser.find_element_by_xpath("/html/body/div[2]/div[1]/section/div/div/div[2]/div/form/div[6]/label/input")
        password.send_keys(m_password)
        
        confirmPassword = self.browser.find_element_by_xpath("/html/body/div[2]/div[1]/section/div/div/div[2]/div/form/div[7]/label/input")
        confirmPassword.send_keys(m_confirmPassword)
        
        
        signin_button = self.browser.find_element_by_xpath("/html/body/div[2]/div[1]/section/div/div/div[2]/div/form/div[8]/button")
        signin_button.submit()
        sleep(5)


    def SaveRequestResults(self, DirPath, signUpCase, ExpectedResult):
        """
        Get Request result and check if compatible with expected result
        """
        if os.path.exists(DirPath) == False:
            os.mkdir(DirPath)
        ActualResult = (self.browser.current_url != self.url)
        if ( ActualResult != ExpectedResult):
            print"[[TEST FAILURE]]"
            image = DirPath+"/"+str(signUpCase["Test_ID"])+".png"
            print"Screenshot for the failed case saved in ",image
            self.browser.get_screenshot_as_file(image)
            return False
        else:
            print"[[TEST SUCCEED]]"
            return True


    def OpenBrowser(self):
        print"Opening browser..."
        self.browser = webdriver.Firefox(executable_path='./geckodriver')
        self.browser.set_window_size(700,1000)
        self.browser.set_window_position(900,0)
        self.browser.get(self.url)
        self.browser.execute_script('document.body.style.MozTransform = "scale(0.80)";')
        self.browser.execute_script('document.body.style.MozTransformOrigin = "0 0";')
        #html = self.browser.find_element_by_tag_name('html')
        #html.send_keys(Keys.PAGE_DOWN)
        self.browser.execute_script("window.scrollTo(0, 300)")

    def CloseBrowser(self):
        print"Closing browser..."
        print"################################################"
        self.browser.close()


