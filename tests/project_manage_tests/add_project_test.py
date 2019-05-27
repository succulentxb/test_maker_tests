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
        start_input = AddProjectTest.driver.find_element_by_id("startDate")
        end_input = AddProjectTest.driver.find_element_by_id("finishDate")

        name_input.send_keys("zhengtest_project")
        start_input.send_keys("2019-05-01")
        end_input.send_keys("2019-06-01")

        submit_btn = AddProjectTest.driver.find_element_by_id("save-project-btn")
        submit_btn.click()

    def test_add_project_illegal(self):
        AddProjectTest.pjs_btn_click()

        create_pj_btn = AddProjectTest.driver.find_element_by_id("create-project-btn")
        assert create_pj_btn is not None
        create_pj_btn.click()

        name_input = AddProjectTest.driver.find_element_by_id("project-name")
        start_input = AddProjectTest.driver.find_element_by_id("startDate")
        end_input = AddProjectTest.driver.find_element_by_id("finishDate")

        name_input.send_keys("zhengtest_project_illegal")
        start_input.send_keys("illegal")
        end_input.send_keys("illegal")

        submit_btn = AddProjectTest.driver.find_element_by_id("save-project-btn")
        submit_btn.click()

    def test_add_project_noparam(self):
        AddProjectTest.pjs_btn_click()

        create_pj_btn = AddProjectTest.driver.find_element_by_id("create-project-btn")
        assert create_pj_btn is not None
        create_pj_btn.click()

        submit_btn = AddProjectTest.driver.find_element_by_id("save-project-btn")
        submit_btn.click()

    def test_add_project_reset(self):
        AddProjectTest.pjs_btn_click()

        create_pj_btn = AddProjectTest.driver.find_element_by_id("create-project-btn")
        assert create_pj_btn is not None
        create_pj_btn.click()

        name_input = AddProjectTest.driver.find_element_by_id("project-name")
        start_input = AddProjectTest.driver.find_element_by_id("startDate")
        end_input = AddProjectTest.driver.find_element_by_id("finishDate")

        name_input.send_keys("to_reset")
        start_input.send_keys("to_reset")
        end_input.send_keys("to_reset")


