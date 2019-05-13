import sys
sys.path.append("./../../")

from tests import setup
import unittest
import time
from selenium import webdriver


class AdminStateTest(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setup(cls):
        if AdminStateTest.driver is None:
            AdminStateTest.driver = setup.admin_setup()
        if setup.ADMIN_INDEX_URL_PREFIX not in AdminStateTest.driver.current_url:
            AdminStateTest.driver.close()
            AdminStateTest.driver = setup.admin_setup()
        assert AdminStateTest.driver is not None

    @classmethod
    def get_user_items(cls):
        if AdminStateTest.driver is None:
            return []
        items = []
        while len(items) == 0:
            try:
                items = AdminStateTest.driver.find_elements_by_css_selector("#user-data-table > tbody > tr")
                time.sleep(1)
            except Exception as e:
                print(e)
        return items

    def test_deactivate_admin(self):
        setup.admin_user_btn_click(AdminStateTest.driver)
        items = AdminStateTest.get_user_items()
        for item in items:
            state = item.find_element_by_css_selector("td:nth-child(8) > span").text
            # 找到第一个管理员用户，设为非管理员
            if state == "管理员":
                checkbox = item.find_element_by_css_selector("td:nth-child(1) > input")
                if checkbox is None:
                    continue
                checkbox.click()
                break
        admin_btn = AdminStateTest.driver.find_element_by_id("switch-admin-btn")
        assert admin_btn is not None
        admin_btn.click()

        btns = setup.get_confirm_box_btns(AdminStateTest.driver)
        btns[1].click()
        setup.success_btn_click(AdminStateTest.driver)
        print("[test_deactivate_admin] test done")

    def test_activate_admin(self):
        setup.admin_user_btn_click(AdminStateTest.driver)
        items = AdminStateTest.get_user_items()
        for item in items:
            state = item.find_element_by_css_selector("td:nth-child(8) > span").text
            if state == "普通用户":
                checkbox = item.find_element_by_css_selector("td:nth-child(1) > input")
                if checkbox is None:
                    continue
                checkbox.click()
                break
        admin_btn = AdminStateTest.driver.find_element_by_id("switch-admin-btn")
        assert admin_btn is not None
        admin_btn.click()

        btns = setup.get_confirm_box_btns(AdminStateTest.driver)
        btns[1].click()
        setup.success_btn_click(AdminStateTest.driver)
        print("[test_activate_admin] test done")

    def test_switch_admins(self):
        setup.admin_user_btn_click(AdminStateTest.driver)
        items = AdminStateTest.get_user_items()
        for i in range(2):
            checkbox = items[i].find_element_by_css_selector("td:nth-child(1) > input")
            if not checkbox:
                continue
            checkbox.click()

        state_btn = AdminStateTest.driver.find_element_by_id("switch-admin-btn")
        assert state_btn is not None
        state_btn.click()

        btns = setup.get_confirm_box_btns(AdminStateTest.driver)
        btns[1].click()
        setup.success_btn_click(AdminStateTest.driver)
        print("[test_switch_admins] test done.")


if __name__ == "__main__":
    try:
        AdminStateTest.setup()

        suite = unittest.TestSuite()
        tests = [AdminStateTest("test_deactivate_admin"), AdminStateTest("test_activate_admin"),
                 AdminStateTest("test_switch_admins"), AdminStateTest("test_switch_admins")]
        suite.addTests(tests)

        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
    finally:
        if AdminStateTest.driver:
            AdminStateTest.driver.close()
