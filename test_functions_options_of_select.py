import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
class Test_Functions_options(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com/')
    def test_functions_option_select(self):
        #定位到设置选项
        setting_option=self.driver.find_element_by_xpath('//*[@id="u1"]/a[8]').click()
        #ActionChains(self.driver).move_to_element(setting_option).perform()
        #self.driver.implicitly_wait(3)
        #选择搜索设置选项
        time.sleep(1)
        search_setting_option=self.driver.find_element_by_xpath("//*[@id='wrapper']/div[6]/a[1]")
        search_setting_option.click()
        time.sleep(1)
        box = Select(self.driver.find_element_by_xpath('//*[@id="nr"]')).select_by_value('20') #选择每页显示20条
        #测试获取的选项和期望的选项是否一致
        time.sleep(2)
        print(box)
        #self.assertEqual(3,len(box))
        print(Select(self.driver.find_element_by_xpath('//*[@id="nr"]')).options)
        print(len(Select(self.driver.find_element_by_xpath('//*[@id="nr"]')).options))
    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    unittest.main(verbosity=2)