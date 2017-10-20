import unittest
import pytest
from selenium import webdriver
from utils.ExcelUtils import ReadExcel


class DataDrivenTesting(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://www.amazon.com")
        cls.driver.maximize_window()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    test_data = [("baby products","babay accessories")]

    @pytest.mark.parametrize("search_value1,serach_value2",test_data)
    def test_ddt(self,search_value1,serach_value2,test_data):
        print("Test Data::::",search_value1)
        self.driver.find_element_by_id("twotabsearchtextbox").send_keys(search_value1)
        self.driver.find_element_by_xpath("//input[@value='Go']").click()




