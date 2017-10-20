import unittest
import nose
from nose_parameterized import parameterized
from  selenium import  webdriver
from utils.ExcelUtils import ReadExcel


class NoseParameterizedDataDrivenTesting(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://www.amazon.com")

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    @parameterized.expand(ReadExcel.get_data())
    def test_ddt_with_nose_parameterized(self,val1):
        print("Test data:::",val1)

        self.driver.find_element_by_id("twotabsearchtextbox").send_keys(val1)
        self.driver.find_element_by_xpath("//input[@value='Go']").click()


