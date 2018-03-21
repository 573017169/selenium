from selenium import webdriver
import unittest
import time

class MyTest(unittest.TestCase):
    '''有道翻译测试'''
    def setUp(self):
        self.driver = webdriver.Firefox()
#        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.youdao.com"

    def test_youdao(self):
        '''翻译：webdriver'''
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("translateContent").click()
        driver.find_element_by_id("translateContent").clear()
        driver.find_element_by_id("translateContent").send_keys("webdriver")
        driver.find_element_by_css_selector("button").click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title,"【webdriver】什么意思_英语webdriver的翻译_音标_读音_用法_例句_在线翻译_有道词典")
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()