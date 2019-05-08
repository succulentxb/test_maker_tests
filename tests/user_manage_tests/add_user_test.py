import sys
sys.path.append("./../../")

from tests.setup import admin_setup
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
    def setup(self):
        AddUserTest.driver = admin_setup()
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

        print(users_btn)
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
        while True:
            print("waiting...")
            time.sleep(1)


if __name__ == "__main__":
    try:
        unittest.main()
    except:
        if AddUserTest.driver:
            AddUserTest.driver.close()
