import sys
sys.path.append("./../../")

from tests import setup
import unittest
import time
from selenium import webdriver

USER_INFO = {
    "username": "ZhengTest",
    "fullname": "ZhengTest",
    "phone": "18702101111",
    "email": "xxx@fudan.edu.cn",
    "password": "password"
}


class AddUserTest(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setup(cls):
        if AddUserTest.driver is None:
            AddUserTest.driver = setup.admin_setup()
        if setup.ADMIN_INDEX_URL_PREFIX not in AddUserTest.driver.current_url:
            AddUserTest.driver.close()
            AddUserTest.driver = setup.admin_setup()
        assert AddUserTest.driver is not None

    def test_add_user_legal(self):
        AddUserTest.setup()
        users_btn = None
        while users_btn is None:
            try:
                time.sleep(1)
                users_btn = AddUserTest.driver.find_element_by_xpath('//*[@id="navigation-panel"]/ul/li[2]/a')
            except Exception as e:
                print(e)
        users_btn.click()

        add_user_btn = None
        while add_user_btn is None:
            try:
                time.sleep(1)
                add_user_btn = AddUserTest.driver.find_element_by_id("create-user-btn")
            except Exception as e:
                print(e)

        add_user_btn.click()

        username_input = None
        # 页面未加载完成，等待加载直到完成
        while username_input is None:
            try:
                time.sleep(1)
                username_input = AddUserTest.driver.find_element_by_id("user-username")
            except Exception as e:
                print(e)

        # 获取用户名后缀，每次插入新用户
        f = open("./test_user_counter", mode="r+")
        suffix = f.readline().strip('\n')
        if not suffix:
            suffix = "1"
        f.seek(0)
        f.write(str(int(suffix)+1))
        f.close()
        username_input.send_keys(USER_INFO["username"]+suffix)

        fullname_input = AddUserTest.driver.find_element_by_id("user-fullName")
        assert fullname_input is not None
        fullname_input.send_keys(USER_INFO["fullname"])

        phone_input = AddUserTest.driver.find_element_by_id("user-phone")
        assert phone_input is not None
        phone_input.send_keys(USER_INFO["phone"])

        email_input = AddUserTest.driver.find_element_by_id("user-email")
        assert email_input is not None
        email_input.send_keys(USER_INFO["email"]+suffix)

        pass_input = AddUserTest.driver.find_element_by_id("user-password")
        assert pass_input is not None
        pass_input.send_keys(USER_INFO["password"])

        pass_confirm_input = AddUserTest.driver.find_element_by_id("user-password-confirm")
        assert pass_confirm_input is not None
        pass_confirm_input.send_keys(USER_INFO["password"])

        submit_btn = AddUserTest.driver.find_element_by_id("submit-form-btn")
        assert submit_btn is not None
        submit_btn.click()

        check_btn = None
        while check_btn is None:
            try:
                time.sleep(1)
                check_btn = AddUserTest.driver.find_elements_by_css_selector(".bootstrap-dialog-footer-buttons > button")
            except Exception as e:
                print(e)
        assert len(check_btn) == 1
        check_btn[0].click()
        print("add_user_legal test done.")

    def test_add_dup_user(self):
        AddUserTest.setup()
        users_btn = None
        while users_btn is None:
            try:
                time.sleep(1)
                users_btn = AddUserTest.driver.find_element_by_xpath('//*[@id="navigation-panel"]/ul/li[2]/a')
            except Exception as e:
                print(e)
        users_btn.click()

        add_user_btn = None
        while add_user_btn is None:
            try:
                time.sleep(1)
                add_user_btn = AddUserTest.driver.find_element_by_id("create-user-btn")
            except Exception as e:
                print(e)

        add_user_btn.click()

        username_input = None
        # 页面未加载完成，等待加载直到完成
        while username_input is None:
            try:
                time.sleep(1)
                username_input = AddUserTest.driver.find_element_by_id("user-username")
            except Exception as e:
                print(e)

        username_input.send_keys(USER_INFO["username"])

        fullname_input = AddUserTest.driver.find_element_by_id("user-fullName")
        assert fullname_input is not None
        fullname_input.send_keys(USER_INFO["fullname"])

        phone_input = AddUserTest.driver.find_element_by_id("user-phone")
        assert phone_input is not None
        phone_input.send_keys(USER_INFO["phone"])

        email_input = AddUserTest.driver.find_element_by_id("user-email")
        assert email_input is not None
        email_input.send_keys(USER_INFO["email"])

        pass_input = AddUserTest.driver.find_element_by_id("user-password")
        assert pass_input is not None
        pass_input.send_keys(USER_INFO["password"])

        pass_confirm_input = AddUserTest.driver.find_element_by_id("user-password-confirm")
        assert pass_confirm_input is not None
        pass_confirm_input.send_keys(USER_INFO["password"])

        submit_btn = AddUserTest.driver.find_element_by_id("submit-form-btn")
        assert submit_btn is not None
        submit_btn.click()

        check_btn = []
        while len(check_btn) == 0:
            try:
                time.sleep(0.5)
                check_btn = AddUserTest.driver.find_elements_by_css_selector(".bootstrap-dialog-footer-buttons > button")
            except Exception as e:
                print(e)
        assert len(check_btn) == 1
        check_btn[0].click()
        print("test_add_dup_user test done.")

    def test_add_user_no_info(self):
        AddUserTest.setup()
        users_btn = None
        while users_btn is None:
            try:
                time.sleep(1)
                users_btn = AddUserTest.driver.find_element_by_xpath('//*[@id="navigation-panel"]/ul/li[2]/a')
            except Exception as e:
                print(e)
        users_btn.click()

        add_user_btn = None
        while add_user_btn is None:
            try:
                time.sleep(1)
                add_user_btn = AddUserTest.driver.find_element_by_id("create-user-btn")
            except Exception as e:
                print(e)

        add_user_btn.click()

        # 页面未加载完成，等待加载直到完成
        submit_btn = None
        while submit_btn is None:
            try:
                time.sleep(1)
                submit_btn = AddUserTest.driver.find_element_by_id("submit-form-btn")
            except Exception as e:
                print(e)
        assert submit_btn is not None
        submit_btn.click()
        print("submit click!")

        time.sleep(1)
        tip = AddUserTest.driver.find_element_by_id("user-username-error")
        assert tip is not None
        print("test_add_dup_user test done.")


    def test_add_user_invalid_info(self):
        AddUserTest.setup()
        users_btn = None
        while users_btn is None:
            try:
                time.sleep(1)
                users_btn = AddUserTest.driver.find_element_by_xpath('//*[@id="navigation-panel"]/ul/li[2]/a')
            except Exception as e:
                print(e)
        users_btn.click()

        add_user_btn = None
        while add_user_btn is None:
            try:
                time.sleep(1)
                add_user_btn = AddUserTest.driver.find_element_by_id("create-user-btn")
            except Exception as e:
                print(e)

        add_user_btn.click()

        username_input = None
        # 页面未加载完成，等待加载直到完成
        while username_input is None:
            try:
                time.sleep(1)
                username_input = AddUserTest.driver.find_element_by_id("user-username")
            except Exception as e:
                print(e)

        # 获取用户名后缀，每次插入新用户
        f = open("./test_user_counter", mode="r+")
        suffix = f.readline().strip('\n')
        if not suffix:
            suffix = "1"
        f.seek(0)
        f.write(str(int(suffix) + 1))
        f.close()
        username_input.send_keys(USER_INFO["username"] + suffix)

        fullname_input = AddUserTest.driver.find_element_by_id("user-fullName")
        assert fullname_input is not None
        fullname_input.send_keys(USER_INFO["fullname"])

        phone_input = AddUserTest.driver.find_element_by_id("user-phone")
        assert phone_input is not None
        phone_input.send_keys(USER_INFO["phone"])

        email_input = AddUserTest.driver.find_element_by_id("user-email")
        assert email_input is not None
        email_input.send_keys("illegal-email")

        pass_input = AddUserTest.driver.find_element_by_id("user-password")
        assert pass_input is not None
        pass_input.send_keys(USER_INFO["password"])

        pass_confirm_input = AddUserTest.driver.find_element_by_id("user-password-confirm")
        assert pass_confirm_input is not None
        pass_confirm_input.send_keys(USER_INFO["password"])

        submit_btn = AddUserTest.driver.find_element_by_id("submit-form-btn")
        assert submit_btn is not None
        submit_btn.click()

        time.sleep(1)
        tip = AddUserTest.driver.find_element_by_id("user-email-error")
        assert tip is not None
        print("add_user_legal test done.")


if __name__ == "__main__":
    try:
        suite = unittest.TestSuite()

        tests = [AddUserTest("test_add_user_invalid_info")]
        suite.addTests(tests)

        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
    except:
        if AddUserTest.driver:
            AddUserTest.driver.close()
