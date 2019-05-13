import sys
sys.path.append("./../../")

from tests import setup
import unittest
import time
from selenium import webdriver


class PassResetTest(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setup(cls):
        if PassResetTest.driver is None:
            PassResetTest.driver = setup.admin_setup()
        if setup.ADMIN_INDEX_URL_PREFIX not in PassResetTest.driver.current_url:
            PassResetTest.driver.close()
            PassResetTest.driver = setup.admin_setup()
        assert PassResetTest.driver is not None

    @classmethod
    def get_user_items(cls):
        if PassResetTest.driver is None:
            return []
        items = []
        while len(items) == 0:
            try:
                items = PassResetTest.driver.find_elements_by_css_selector("#user-data-table > tbody > tr")
                time.sleep(1)
            except Exception as e:
                print(e)
        return items

    def test_reset_one_user(self):
        setup.admin_user_btn_click(PassResetTest.driver)
        items = PassResetTest.get_user_items()
        assert len(items) > 0
        checkbox = items[0].find_element_by_css_selector("td:nth-child(1) > input")
        assert checkbox is not None
        checkbox.click()

        reset_btn = PassResetTest.driver.find_element_by_id("reset-password-btn")
        assert reset_btn is not None
        reset_btn.click()

        btns = setup.get_confirm_box_btns(PassResetTest.driver)
        btns[1].click()
        setup.success_btn_click(PassResetTest.driver)
        print("[test_reset_one_user] test done.")

    def test_reset_users(self):
        setup.admin_user_btn_click(PassResetTest.driver)
        items = PassResetTest.get_user_items()
        assert len(items) > 0
        for i in range(2):
            checkbox = items[i].find_element_by_css_selector("td:nth-child(1) > input")
            assert checkbox is not None
            checkbox.click()

        reset_btn = PassResetTest.driver.find_element_by_id("reset-password-btn")
        assert reset_btn is not None
        reset_btn.click()

        btns = setup.get_confirm_box_btns(PassResetTest.driver)
        btns[1].click()
        setup.success_btn_click(PassResetTest.driver)
        print("[test_reset_users] test done.")


if __name__ == "__main__":
    try:
        PassResetTest.setup()

        suite = unittest.TestSuite()
        tests = [PassResetTest("test_reset_one_user"), PassResetTest("test_reset_users")]
        suite.addTests(tests)

        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
    finally:
        if PassResetTest.driver:
            PassResetTest.driver.close()
