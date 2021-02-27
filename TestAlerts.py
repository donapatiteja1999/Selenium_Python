from selenium import webdriver
from time import sleep
import unittest



class alert(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\cromedriver\chromedriver_win32\chromedriver.exe')
        self.driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
        sleep(3)


    def testAlert_1(self):
        driver=self.driver
        sleep(1)
        driver.maximize_window()
        btn=driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/button')
        btn.click()
        sleep(1)
        alert = driver.switch_to_alert()
        alert.accept()
        sleep(2)
        print("testalert1 passed")

    def testAlert_2(self):
        driver=self.driver
        sleep(1)
        driver.maximize_window()
        btn=driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/button')
        msg=driver.find_element_by_id('confirm-demo')
        sleep(1)
        btn.click()
        alert=driver.switch_to_alert()
        sleep(1)
        alert.accept()
        sleep(1)
        assert msg.text=="You pressed OK!"
        btn.click()
        sleep(1)
        alert=driver.switch_to_alert()
        sleep(1)
        alert.dismiss()
        sleep(1)
        assert msg.text=="You pressed Cancel!"
        print("Testalert2 passed")


    def testAlert_3(self):
        driver=self.driver
        driver.maximize_window()
        btn=driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[3]/div[2]/button')
        msg=driver.find_element_by_id('prompt-demo')
        sleep(1)
        btn.click()
        alert=driver.switch_to_alert()
        sleep(1)
        alert.send_keys("python programming")
        sleep(3)
        alert.accept()
        sleep(1)
        assert msg.text=="You have entered 'python programming' !"
        print("TestAlert3 passed")



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

