from selenium import webdriver
import unittest  #导入单元测试模块
#创建一个注册新用户的类
class RegisterNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://www.imooc.com/')
    #检查登录按钮是否可见且可用,是否可以正常登录
    def test_login(self):
        login= self.driver.find_element_by_link_text('登录')
        self.assertTrue(login.is_enabled())
        login.click()
        username=self.driver.find_element_by_name('email')
        self.assertTrue(username.is_displayed())
        username.clear()
        username.send_keys('1101055805@qq.com')
        password = self.driver.find_element_by_name('password')
        self.assertTrue(password.is_enabled())
        password.clear()
        password.send_keys('xjm12054026520')
        button=self.driver.find_element_by_xpath('//*[@id="auto-signin"]')
        self.assertTrue(button.is_displayed() and button.is_enabled())
        button.click()
        login_button=self.driver.find_element_by_xpath('//*[@id="signup-form"]/div[5]/input')
        login_button.click()
    #添加一个测试方法test_register_new_user(self)到类中，创建一个注册测试方法
    def test_register_new_user(self):
        register=self.driver.find_element_by_link_text('注册')
        #定位到注册的账号
        account_number=self.driver.find_element_by_xpath('//*[@id="signup-form pr"]/div[1]/input')
        #get_attribute用于获取元素的属性值
        self.assertEqual('37',account_number.get_attribute('maxlength'))
        #定位到注册的验证码


        #is_selected方法用于检查单选按钮和复选框，此测试用例用于检查复选框是否默认的未被选中的情况
        Check_box=self.driver.find_element_by_id('signup-protocol')
        self.assertFalse(Check_box.is_selected())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

