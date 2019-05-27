import sys
sys.path.append("./../../")

from tests import setup
import unittest
import time
from selenium import webdriver


class PjInfoTest(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setup(cls):
        if PjInfoTest.driver is None:
            PjInfoTest.driver = setup.admin_setup()
        if setup.ADMIN_INDEX_URL_PREFIX not in PjInfoTest.driver.current_url:
            PjInfoTest.driver.close()
            PjInfoTest.driver = setup.admin_setup()
        assert PjInfoTest.driver is not None

    @classmethod
    def pjs_btn_click(cls):
        pjs_btn = None
        while pjs_btn is None:
            try:
                pjs_btn = PjInfoTest.driver.find_element_by_xpath('//*[@id="navigation-panel"]/ul/li[3]/a')
                time.sleep(1)
            except Exception as e:
                print(e)
        pjs_btn.click()

    def modify_pj_info(self):
        PjInfoTest.pjs_btn_click()

        first_item_modify_btn = PjInfoTest.driver.find_element_by_css_selector(
            "#project-table-body > tr:nth-child(1) > td:nth-child(10) > a.edit-item > i")
        assert first_item_modify_btn is not None
        first_item_modify_btn.click()

        name_input = PjInfoTest.driver.find_element_by_id("project-name")
        assert name_input is not None
        start_input = PjInfoTest.driver.find_element_by_id("startDate")
        assert start_input is not None
        end_input = PjInfoTest.driver.find_element_by_id("endDate")
        assert end_input is not None

        name_input.send_keys("zhengtest_modify_pj_name")
        start_input.send_keys("2019-05-01")
        end_input.send_keys("2019-06-01")

        submit_btn = PjInfoTest.driver.find_element_by_id("save-project-btn")
        assert submit_btn is not None
        submit_btn.click()

    def test_modify_pj_illegal(self):
        PjInfoTest.pjs_btn_click()

        first_item_modify_btn = PjInfoTest.driver.find_element_by_css_selector(
            "#project-table-body > tr:nth-child(1) > td:nth-child(10) > a.edit-item > i")
        assert first_item_modify_btn is not None
        first_item_modify_btn.click()

        name_input = PjInfoTest.driver.find_element_by_id("project-name")
        assert name_input is not None
        start_input = PjInfoTest.driver.find_element_by_id("startDate")
        assert start_input is not None
        end_input = PjInfoTest.driver.find_element_by_id("endDate")
        assert end_input is not None

        name_input.send_keys("zhengtest_modify_pj_name")
        start_input.send_keys("illegal")
        end_input.send_keys("illegal")

        submit_btn = PjInfoTest.driver.find_element_by_id("save-project-btn")
        assert submit_btn is not None
        submit_btn.click()

    def test_modify_pj_null(self):
        PjInfoTest.pjs_btn_click()

        first_item_modify_btn = PjInfoTest.driver.find_element_by_css_selector(
            "#project-table-body > tr:nth-child(1) > td:nth-child(10) > a.edit-item > i")
        assert first_item_modify_btn is not None
        first_item_modify_btn.click()

        name_input = PjInfoTest.driver.find_element_by_id("project-name")
        assert name_input is not None
        start_input = PjInfoTest.driver.find_element_by_id("startDate")
        assert start_input is not None
        end_input = PjInfoTest.driver.find_element_by_id("endDate")
        assert end_input is not None

        name_input.send_keys("")
        start_input.send_keys("")
        end_input.send_keys("")

        submit_btn = PjInfoTest.driver.find_element_by_id("save-project-btn")
        assert submit_btn is not None
        submit_btn.click()


if __name__ == "__main__":
    try:
        PjInfoTest.setup()

        suite = unittest.TestSuite()
        suite.addTests([PjInfoTest("test_modify_pj_null")])

        runner = unittest.TextTestRunner()
        runner.run(suite)
    finally:
        if PjInfoTest.driver:
            PjInfoTest.driver.close()
