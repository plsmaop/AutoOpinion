import time
import getpass
from copy import deepcopy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions 

# http://www.obeythetestinggoat.com/how-to-get-selenium-to-wait-for-page-load-after-a-click.html
# very helpful trick

class AutoOpinion:
    def __init__(self):
        self.message = ''
        self.browser = webdriver.PhantomJS()

    def login(self):
        self.browser.get('https://investea.aca.ntu.edu.tw/aca_doc/midopin/midopinion.asp')
        print('=========================================================================================')
        print('\n')
        try:
            ID = self.browser.find_element_by_name("user")
        except:
            print("The Server is Down, Please Try Again Later")
            exit(1)
        password = self.browser.find_element_by_name("pass")
        ID.clear()
        password.clear()
        ID.send_keys(input('Please Enter Your Student ID: '))
        password.send_keys(getpass.getpass('Please Enter Your Password: '))
        self.message = input('Please Enter the Response You Want to Fill(responses for all classes will be the same): ')
        self.browser.find_element_by_name("Submit").click()
        while True:
            if (str(self.browser.title)).find('教學意見調查系統') != -1:
                print('Login Success!!')
                break
            elif (str(self.browser.find_element_by_tag_name('body').text)).find('登入失敗') != -1:
                print('Login Failed!!\nPlease re-enter your ID and Password')
                self.login()
                break
    
    def fillOpinion(self):
        self.browser.find_element_by_name("submit").click()
        WebDriverWait(self.browser, 15).until(
            expected_conditions.title_contains('學期課程'))
            
        courseIndex = 0
        yourCourses = self.browser.find_elements_by_xpath("//input[@type='radio']")
        while courseIndex < len(yourCourses):
            currentUrl = str(self.browser.current_url)
            yourCourses = self.browser.find_elements_by_xpath("//input[@type='radio']")
            select = self.browser.find_element_by_name("SubmitForm")
            course = yourCourses[courseIndex]
            courseID = ("Course ID: " + str(course.get_attribute("value")) + " DONE!!")
            course.click()
            select.click()
            WebDriverWait(self.browser, 15).until(expected_conditions.url_changes(currentUrl))
            
            currentUrl = str(self.browser.current_url)
            self.browser.find_element_by_tag_name('textarea').send_keys(self.message)
            self.browser.find_element_by_xpath("//input[@type='Submit']").click()
            WebDriverWait(self.browser, 15).until(expected_conditions.url_changes(currentUrl))
            
            currentUrl = str(self.browser.current_url)
            self.browser.find_element_by_xpath("//input[@type='submit']").click()
            WebDriverWait(self.browser, 15).until(expected_conditions.url_changes(currentUrl))
            
            courseIndex += 1
            print (courseID)
        print('ALL WORKS DONE!!')
        self.browser.close()  

def main():
    if __name__ == '__main__':
        test = AutoOpinion()
        test.login()
        test.fillOpinion()

main()
        