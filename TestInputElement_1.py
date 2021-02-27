from selenium import webdriver
from time import sleep
import unittest


class InputElement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\cromedriver\chromedriver_win32\chromedriver.exe')
        self.driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
        sleep(3)


    def testSingleInputElement(self):
        driver=self.driver
        driver.maximize_window()
        inputElement=driver.find_element_by_id("user-message")
        showMsgBtn = driver.find_element_by_xpath("//*[@id='get-input']/button")
        a=["hi","Hello","How are you?"]
        for i in a:
            sleep(2)
            inputElement.clear()
            sleep(1.5)
            inputElement.send_keys(i)
            sleep(2)
            showMsgBtn.click()
            sleep(2)

    def testMultiInputElements(self):
        driver = self.driver
        driver.maximize_window()
        inputElement1 = driver.find_element_by_id("sum1")
        inputElement2 = driver.find_element_by_id("sum2")
        showMsgBtn = driver.find_element_by_xpath("//*[@id='gettotal']/button")
        result=driver.find_element_by_id("displayvalue")
        for i in range(4):
            sleep(1)
            inputElement1.clear()
            inputElement2.clear()
            inputElement1.send_keys(i)
            sleep(1)
            inputElement2.send_keys(i)
            sleep(2)
            showMsgBtn.click()
            assert int(result.text)==(i+i)
            sleep(2)


    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
