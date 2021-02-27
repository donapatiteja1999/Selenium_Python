from selenium import webdriver
from time import sleep
import unittest

class radioButton(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\cromedriver\chromedriver_win32\chromedriver.exe')
        self.driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")
        sleep(3)

    def testRadioBtnOfOneGroup(self):
        driver=self.driver
        RbtnMale=driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/label[1]/input')
        RbtnFeMale=driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/label[2]/input')
        sleep(1)
        RbtnMale.click()
        sleep(1)
        assert RbtnMale.is_selected()==True
        assert RbtnFeMale.is_selected()==False
        checkBtn=driver.find_element_by_id("buttoncheck")
        sleep(1)
        checkBtn.click()
        textDisplayed=driver.find_element_by_class_name("radiobutton")
        sleep(1)
        assert textDisplayed.text=="Radio button 'Male' is checked"
        RbtnFeMale.click()
        sleep(1)
        assert RbtnMale.is_selected() ==False
        assert RbtnFeMale.is_selected() ==True
        checkBtn.click()
        sleep(1)
        assert textDisplayed.text == "Radio button 'Female' is checked"



    def tear_down(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()



