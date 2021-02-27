from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.support.ui import Select
class dropDown(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\cromedriver\chromedriver_win32\chromedriver.exe')
        self.driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
        sleep(3)

    def testDropDown1(self):
        driver=self.driver
        driver.maximize_window()
        list=driver.find_element_by_id("select-demo")
        list.click()
        select=Select(list)
        sleep(1)
        message=driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/p[2]')
        select.select_by_value("Monday")
        sleep(1)
        assert "Day selected :- Monday"==message.text

    def testDropDown2(self):
        driver = self.driver
        driver.maximize_window()
        list = driver.find_element_by_id("multi-select")
        list.click()
        select = Select(list)
        sleep(1)
        btn=driver.find_element_by_id("printMe")
        message=driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/p[2]')
        options=["Ohio","New York","Texas"]
        for i in options:
            select.select_by_value(i)
            sleep(1.5)
            btn.click()
            sleep(0.5)
            assert "First selected option is : "+i == message.text
            select.deselect_by_value(i)

    def tear_down(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()
