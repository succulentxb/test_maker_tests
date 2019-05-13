import sys
sys.path.append("./../../")

from tests import setup
import unittest
import time
from selenium import webdriver

CLIENT_URL = "http://gc21131138.imwork.net:20430/test-maker/web/client/index.action"

USER_INFO = {
    "fullname": "lxb",
    "email": "test@fudan.edu.cn",
    "phone": "123123123"
}

class NaviTest(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setup(cls):
        if NaviTest.driver is None:
            NaviTest.driver = setup.admin_setup()
        if setup.ADMIN_INDEX_URL_PREFIX not in NaviTest.driver.current_url:
            NaviTest.driver.close()
            NaviTest.driver = setup.admin_setup()
        assert NaviTest.driver is not None

    def test_logo(self):
        logo = None
        while logo is None:
            try:
                logo = NaviTest.driver.find_element_by_xpath('//*[@id="navbar"]/a')
                if logo is None:
                    time.sleep(1)
            except Exception as e:
                print(e)
                time.sleep(1)
        assert logo is not None
        logo.click()
        time.sleep(1)
        handles = NaviTest.driver.window_handles
        assert len(handles) == 2

    def test_update_info(self):
        time.sleep(1)
        info_btn = NaviTest.driver.find_element_by_css_selector("#navbar > ul > li:nth-child(2) > a")
        assert info_btn is not None
        info_btn.click()
        update_btn = NaviTest.driver.find_element_by_css_selector("#navbar > ul > li.dropdown.open > ul > li:nth-child(1) > a")
        assert update_btn is not None
        update_btn.click()

        fullname_input = NaviTest.driver.find_element_by_id("fullName")
        email_input = NaviTest.driver.find_element_by_id("email")
        phone = NaviTest.driver.find_element_by_id("phone")

        assert fullname_input is not None
        assert email_input is not None
        assert phone is not None

        fullname_input.send_keys(USER_INFO["fullname"])
        email_input.send_keys(USER_INFO["email"])
        phone.send_keys(USER_INFO["phone"])

        submit_btn = NaviTest.driver.find_element_by_id("submit-profile-form-btn")
        assert submit_btn is not None
        submit_btn.click()
        setup.success_btn_click(NaviTest.driver)
        print("[test_update_info] test done")

    def test_update_info_illegal_param(self):
        time.sleep(1)
        info_btn = NaviTest.driver.find_element_by_css_selector("#navbar > ul > li:nth-child(2) > a")
        assert info_btn is not None
        info_btn.click()
        update_btn = NaviTest.driver.find_element_by_css_selector("#navbar > ul > li.dropdown.open > ul > li:nth-child(1) > a")
        assert update_btn is not None
        update_btn.click()

        fullname_input = NaviTest.driver.find_element_by_id("fullName")
        email_input = NaviTest.driver.find_element_by_id("email")
        phone = NaviTest.driver.find_element_by_id("phone")

        assert fullname_input is not None
        assert email_input is not None
        assert phone is not None

        fullname_input.send_keys(USER_INFO["fullname"])
        email_input.send_keys("illegal")
        phone.send_keys(USER_INFO["phone"])

        submit_btn = NaviTest.driver.find_element_by_id("submit-profile-form-btn")
        assert submit_btn is not None
        submit_btn.click()
        setup.success_btn_click(NaviTest.driver)
        print("[test_update_info_illegal_param] test done")

    def test_update_info_no_param(self):
        time.sleep(1)
        info_btn = NaviTest.driver.find_element_by_css_selector("#navbar > ul > li:nth-child(2) > a")
        assert info_btn is not None
        info_btn.click()
        update_btn = NaviTest.driver.find_element_by_css_selector("#navbar > ul > li.dropdown.open > ul > li:nth-child(1) > a")
        assert update_btn is not None
        update_btn.click()

        submit_btn = NaviTest.driver.find_element_by_id("submit-profile-form-btn")
        assert submit_btn is not None
        submit_btn.click()
        setup.success_btn_click(NaviTest.driver)
        print("[test_update_info_no_param] test done")

    def test_pass_modify(self):
        time.sleep(1)
        info_btn = NaviTest.driver.find_element_by_css_selector("#navbar > ul > li:nth-child(2) > a")
        assert info_btn is not None
        info_btn.click()
        modify_btn = NaviTest.driver.find_element_by_css_selector("#navbar > ul > li.dropdown.open > ul > li:nth-child(2) > a")
        assert modify_btn is not None
        modify_btn.click()

        old_pass_input = NaviTest.driver.find_element_by_id("oldPassword")
        new_pass_input = NaviTest.driver.find_element_by_id("newPassword")
        retype_pass_input = NaviTest.driver.find_element_by_id("retypePassword")
        submit_btn = NaviTest.driver.find_element_by_id("change-passwd-submit")

        assert not (old_pass_input is None or new_pass_input is None or retype_pass_input is None or submit_btn is None)
        old_pass_input.send_keys("123456")
        new_pass_input.send_keys("123456")
        retype_pass_input.send_keys("123456")
        submit_btn.click()

        setup.success_btn_click(NaviTest.driver)
        print("[test_pass_modify] test done")

    def test_pass_modify_incorrect_pass(self):
        time.sleep(1)
        info_btn = NaviTest.driver.find_element_by_css_selector("#navbar > ul > li:nth-child(2) > a")
        assert info_btn is not None
        info_btn.click()
        modify_btn = NaviTest.driver.find_element_by_css_selector("#navbar > ul > li.dropdown.open > ul > li:nth-child(2) > a")
        assert modify_btn is not None
        modify_btn.click()

        old_pass_input = NaviTest.driver.find_element_by_id("oldPassword")
        new_pass_input = NaviTest.driver.find_element_by_id("newPassword")
        retype_pass_input = NaviTest.driver.find_element_by_id("retypePassword")
        submit_btn = NaviTest.driver.find_element_by_id("change-passwd-submit")

        assert not (old_pass_input is None or new_pass_input is None or retype_pass_input is None or submit_btn is None)
        old_pass_input.send_keys("incorrect")
        new_pass_input.send_keys("123456")
        retype_pass_input.send_keys("123456")
        submit_btn.click()

        setup.success_btn_click(NaviTest.driver)
        print("[test_pass_modify_incorrect_pass] test done")

    def test_pass_modify_no_param(self):
        time.sleep(1)
        info_btn = NaviTest.driver.find_element_by_css_selector("#navbar > ul > li:nth-child(2) > a")
        assert info_btn is not None
        info_btn.click()
        modify_btn = NaviTest.driver.find_element_by_css_selector("#navbar > ul > li.dropdown.open > ul > li:nth-child(2) > a")
        assert modify_btn is not None
        modify_btn.click()

        submit_btn = NaviTest.driver.find_element_by_id("change-passwd-submit")
        assert submit_btn is not None
        submit_btn.click()

        setup.success_btn_click(NaviTest.driver)
        print("[test_pass_modify_incorrect_pass] test done")

    def test_help_info(self):
        time.sleep(1)
        help_btn = NaviTest.driver.find_element_by_css_selector("#navbar > ul > li:nth-child(3) > a")
        assert help_btn is not None
        help_btn.click()
        about_btn = NaviTest.driver.find_element_by_css_selector("#navbar > ul > li.dropdown.open > ul > li > a")
        assert about_btn is not None

        confirm_btn = NaviTest.driver.find_element_by_css_selector("#about-dialog > div > div > div.modal-footer > button")
        assert confirm_btn is not None
        confirm_btn.click()
        print("[test_help_info] test done")

    def test_logout(self):
        time.sleep(1)
        logout_btn = NaviTest.driver.find_element_by_id("logout-btn")
        assert logout_btn is not None
        logout_btn.click()
        time.sleep(1)
        assert NaviTest.driver.current_url == setup.ADMIN_INDEX_URL


if __name__ == "__main__":
    try:
        NaviTest.setup()

        suite = unittest.TestSuite()
        suite.addTests([NaviTest("test_update_info")])

        runner = unittest.TextTestRunner()
        runner.run(suite)
    finally:
        if NaviTest.driver:
            NaviTest.driver.close()
