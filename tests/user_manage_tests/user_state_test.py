import sys
sys.path.append("./../../")

from tests import setup
import unittest
import time
from selenium import webdriver


class UserStateTest(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setup(cls):
        if UserStateTest.driver is None:
            UserStateTest.driver = setup.admin_setup()
        if setup.ADMIN_INDEX_URL_PREFIX not in UserStateTest.driver.current_url:
            UserStateTest.driver.close()
            UserStateTest.driver = setup.admin_setup()
        assert UserStateTest.driver is not None

    @classmethod
    def get_user_items(cls):
        if UserStateTest.driver is None:
            return []
        items = []
        while len(items) == 0:
            try:
                items = UserStateTest.driver.find_elements_by_css_selector("#user-data-table > tbody > tr")
                time.sleep(1)
            except Exception as e:
                print(e)
        return items

    def test_deactivate_user(self):
        setup.admin_user_btn_click(UserStateTest.driver)
        items = UserStateTest.get_user_items()
        for item in items:
            state = item.find_element_by_css_selector("td:nth-child(7) > span").text
            # 找到第一个活动用户，禁用
            if state == "活动":
                checkbox = item.find_element_by_css_selector("td:nth-child(1) > input")
                if checkbox is None:
                    continue
                checkbox.click()
                break
        state_btn = UserStateTest.driver.find_element_by_id("switch-state-btn")
        assert state_btn is not None
        state_btn.click()

        btns = setup.get_confirm_box_btns(UserStateTest.driver)
        btns[1].click()
        setup.success_btn_click(UserStateTest.driver)
        print("test_deactivate_user test done")

    def test_activate_user(self):
        setup.admin_user_btn_click(UserStateTest.driver)
        items = UserStateTest.get_user_items()
        for item in items:
            state = item.find_element_by_css_selector("td:nth-child(7) > span").text
            if state == "已禁用":
                checkbox = item.find_element_by_css_selector("td:nth-child(1) > input")
                if checkbox is None:
                    continue
                checkbox.click()
                break
        state_btn = UserStateTest.driver.find_element_by_id("switch-state-btn")
        assert state_btn is not None
        state_btn.click()

        btns = setup.get_confirm_box_btns(UserStateTest.driver)
        btns[1].click()
        setup.success_btn_click(UserStateTest.driver)
        print("test_deactivate_user test done")

    def test_switch_users(self):
        setup.admin_user_btn_click(UserStateTest.driver)
        items = UserStateTest.get_user_items()
        for i in range(2):
            checkbox = items[i].find_element_by_css_selector("td:nth-child(1) > input")
            if not checkbox:
                continue
            checkbox.click()

        state_btn = UserStateTest.driver.find_element_by_id("switch-state-btn")
        assert state_btn is not None
        state_btn.click()

        btns = setup.get_confirm_box_btns(UserStateTest.driver)
        btns[1].click()
        setup.success_btn_click(UserStateTest.driver)
        print("[test_switch_users] test done.")


if __name__ == "__main__":
    try:
        UserStateTest.setup()

        suite = unittest.TestSuite()
        tests = [UserStateTest("test_deactivate_user"), UserStateTest("test_activate_user"),
                 UserStateTest("test_switch_users"), UserStateTest("test_switch_users")]
        suite.addTests(tests)

        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
    finally:
        if UserStateTest.driver:
            UserStateTest.driver.close()
