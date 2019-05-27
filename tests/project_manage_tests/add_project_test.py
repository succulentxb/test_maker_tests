import sys
sys.path.append("./../../")

from tests import setup
import unittest
import time
from selenium import webdriver


class AddProjectTest(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setup(cls):
        if AddProjectTest.driver is None:
            AddProjectTest.driver = setup.admin_setup()
        if setup.ADMIN_INDEX_URL_PREFIX not in AddProjectTest.driver.current_url:
            AddProjectTest.driver.close()
            AddProjectTest.driver = setup.admin_setup()
        assert AddProjectTest.driver is not None

    @classmethod
    def pjs_btn_click(self):
        pjs_btn = None
        while pjs_btn is None:
            try:
                pjs_btn = AddProjectTest.driver.find_element_by_xpath('//*[@id="navigation-panel"]/ul/li[3]/a')
                time.sleep(1)
            except Exception as e:
                print(e)
        pjs_btn.click()

    def test_add_project(self):
        AddProjectTest.pjs_btn_click()

        create_pj_btn = AddProjectTest.driver.find_element_by_id("create-project-btn")
        assert create_pj_btn is not None
        create_pj_btn.click()

        name_input = AddProjectTest.driver.find_element_by_id("project-name")
        assert name_input is not None
        start_input = AddProjectTest.driver.find_element_by_id("startDate")
        assert start_input is not None
        end_input = AddProjectTest.driver.find_element_by_id("finishDate")
        assert end_input is not None

        name_input.send_keys("zhengtest_project")
        start_input.send_keys("2019-05-01")
        end_input.send_keys("2019-06-01")

        submit_btn = AddProjectTest.driver.find_element_by_id("save-project-btn")
        assert submit_btn is not None
        submit_btn.click()

    def test_add_project_illegal(self):
        AddProjectTest.pjs_btn_click()

        create_pj_btn = AddProjectTest.driver.find_element_by_id("create-project-btn")
        assert create_pj_btn is not None
        create_pj_btn.click()

        name_input = AddProjectTest.driver.find_element_by_id("project-name")
        assert name_input is not None
        start_input = AddProjectTest.driver.find_element_by_id("startDate")
        assert start_input is not None
        end_input = AddProjectTest.driver.find_element_by_id("finishDate")
        assert end_input is not None

        name_input.send_keys("zhengtest_project_illegal")
        start_input.send_keys("illegal")
        end_input.send_keys("illegal")

        submit_btn = AddProjectTest.driver.find_element_by_id("save-project-btn")
        assert submit_btn is not None
        submit_btn.click()

    def test_add_project_noparam(self):
        AddProjectTest.pjs_btn_click()

        create_pj_btn = AddProjectTest.driver.find_element_by_id("create-project-btn")
        assert create_pj_btn is not None
        create_pj_btn.click()

        submit_btn = AddProjectTest.driver.find_element_by_id("save-project-btn")
        assert submit_btn is not None
        submit_btn.click()

    def test_add_project_reset(self):
        AddProjectTest.pjs_btn_click()

        create_pj_btn = AddProjectTest.driver.find_element_by_id("create-project-btn")
        assert create_pj_btn is not None
        create_pj_btn.click()

        name_input = AddProjectTest.driver.find_element_by_id("project-name")
        assert name_input is not None
        start_input = AddProjectTest.driver.find_element_by_id("startDate")
        assert start_input is not None
        end_input = AddProjectTest.driver.find_element_by_id("finishDate")
        assert end_input is not None

        name_input.send_keys("to_reset")
        start_input.send_keys("to_reset")
        end_input.send_keys("to_reset")

        reset_btn = AddProjectTest.driver.find_element_by_css_selector("#adm-save-project-form > fieldset > div:nth-child(6) > div:nth-child(2) > button")
        assert reset_btn is not None
        reset_btn.click()
        assert name_input.get_property("value") == ""
        assert start_input.get_property("value") == ""
        assert end_input.get_property("value") == ""


if __name__ == "__main__":
    try:
        AddProjectTest.setup()

        suite = unittest.TestSuite()
        suite.addTests([AddProjectTest("test_add_project_reset")])

        runner = unittest.TextTestRunner()
        runner.run(suite)
    finally:
        if AddProjectTest.driver:
            AddProjectTest.driver.close()
