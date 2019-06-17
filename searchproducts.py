import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class SearchTests(unittest.TestCase):
    @classmethod
    # first execute from setup() everytime
    def setUpClass(cls):
        #create a chrome session
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()
        # navigate to the application home page
        cls.driver.get("http://demo.magentocommerce.com.com/")
    def test_search_by_category(self):
        #get the search textbox
        self.search_field=self.driver.find_element_by_id("search-main")
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys("phones")
        self.search_field.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(5)
        # get all the anchor elements which have product names
        #displayed currently on result page method
        #find_elemenrs_by_xpath
        products = self.driver.find_element_by_xpath('//h2[@class="search--results-title"]').text
        self.driver.implicitly_wait(1000)
        print("found",str(len(products)),"products in all")
        # Verify expected results
        self.assertEqual(95,len(products))
    @classmethod
    def tearDownClass(cls):
        # Clean up the initialization in setup(), here is to close the chrome browser
        cls.driver.quit()
if __name__=='__main__':
        unittest.main()






