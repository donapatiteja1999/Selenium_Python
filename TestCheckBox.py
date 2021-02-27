from selenium import webdriver
from time import sleep
import unittest


class CheckBox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\cromedriver\chromedriver_win32\chromedriver.exe')
        self.driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
        sleep(3)

    def testsingleCheckBox(self):
        driver=self.driver
        chkBox=driver.find_element_by_id("isAgeSelected")
        driver.maximize_window()
        sleep(2)
        chkBox.click()
        sleep(1.5)
        msgText=driver.find_element_by_id("txtAge")
        assert msgText.text=="Success - Check box is checked"
        chkBox.click()
        sleep(1.5)
        assert msgText.text==""


    def testingClickAllButton(self):
        driver=self.driver
        driver.maximize_window()
        sleep(2)
        btn=driver.find_element_by_id("check1")
        btn.click()
        sleep(2)
        assert btn.get_attribute("value")=="Uncheck All"
        for i in range(1,5):
            sleep(1)
            chkBox=driver.find_element_by_xpath("//*[@id='easycont']/div/div[2]/div[2]/div[2]/div["+str(i)+"]/label/input")
            chkBox.click()
            a=chkBox.is_selected()
            assert a==False
            assert btn.get_attribute("value") == "Check All"
            sleep(1)
        sleep(1)
        assert btn.get_attribute("value")=="Check All"


    def tear_down(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

