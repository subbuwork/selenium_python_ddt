import unittest
import nose
from ddt import ddt, data,file_data, unpack
from selenium import webdriver
from utils.ExcelUtils import ReadExcel


@ddt
class DataDrivenTesting(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://www.amazon.com")
        cls.driver.maximize_window()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    @data(["baby products","baby accessories"],["iphone 7s plub","Moto g"])
    @unpack
    def test_ddt(self,search_value1,search_value2):
        print("Test Data1::::",search_value1)
        print("Test Data2::::",search_value2)
        self.driver.find_element_by_id("twotabsearchtextbox").send_keys(search_value1)
        self.driver.find_element_by_xpath("//input[@value='Go']").click()




