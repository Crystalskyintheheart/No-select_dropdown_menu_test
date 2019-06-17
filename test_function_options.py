from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import sys
#测试一个下拉菜单的功能是否正确
class Test_Function_Optons(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://www.imooc.com/')
    def test_function_options(self):
        exp_option=['微服务','区块链','以太坊','人工智能','机器学习','深度学习','计算机视觉','自然语言处理','数据分析&挖掘']
        actual_option=[]
        #定位元素
        select_functions=self.driver.find_element_by_css_selector('#main > div.bgfff.banner-box > div > div.menuContent > div:nth-child(1) > a > span')
        #检查下拉菜单中有几个选项
        ActionChains(self.driver).move_to_element(select_functions).perform()
        select_functions_alloptions = select_functions.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[2]/div[1]/div/div/div/div[2]').text
        #print(select_functions_alloptions)
        new_select_functions_alloptions=str(select_functions_alloptions).split(' ')
        print(new_select_functions_alloptions)
        #首先测试下拉菜单里面的元素个数是否正确
        self.assertEqual(4,len(new_select_functions_alloptions))
        #然后测试下拉菜单里面的每个元素是否正确
        for option in new_select_functions_alloptions:
            actual_option.append(option)
        #检查实际下拉菜单和期望的下拉菜单是否一致
        self.assertEqual(exp_option,actual_option)
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
        unittest.main(verbosity=2)
