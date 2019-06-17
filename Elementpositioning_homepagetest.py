import  unittest
from selenium import webdriver
class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #cretate a new Chrome session
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver.get('http://demo.magentocommerce.com.com/')
    def test_search_text_field_max_length(self):
        #get the search textbox
        search_field = self.driver.find_element_by_id('search-main')
        #check maxlength attribute is set to 128
        self.assertTrue(search_field.is_enabled())
    def test_search_button_enabled(self):
        #get the search button
        search_button = self.driver.find_element_by_class_name('icon--enter-arrow')
        #check the button is or not ok
        self.assertTrue(search_button.is_enabled())
    def test_my_account_link_is_diaplayed(self):
        #get the account line
        account_link = self.driver.find_element_by_xpath('/html/body/footer/nav/div/div/div[5]/ul/li/strong')
        #check the account line is or not display on the homepage
        self.assertTrue(account_link.is_displayed())
    def test_Finance_field_is_displayed(self):
        Finance_field=self.driver.find_element_by_xpath('//*[@id="public-app"]/div/div/div/div[2]/div/div/div[2]/a/img')
        self.assertTrue(Finance_field.is_displayed())
    @classmethod
    def tearDownClass(cls):
        #close the broswer window
        cls.driver.quit()
if __name__=='__main__':
    unittest.main(verbosity=2)