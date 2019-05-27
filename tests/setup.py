from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

ADMIN_INDEX_URL_PREFIX = "http://gc21131138.imwork.net:20430/test-maker/web/admin"
MAIN_INDEX_URL_PREFIX = "http://gc21131138.imwork.net:20430/test-maker/web/client"
ADMIN_INDEX_URL = "http://gc21131138.imwork.net:20430/test-maker/web/admin/index.action"
MAIN_INDEX_URL = "http://gc21131138.imwork.net:20430/test-maker/web/client/index.action"

USERNAME = "zheng5"
PASSWORD = "123456"
GROUP_NAME = "ZhengGroup"


def admin_setup():
    driver = webdriver.Chrome()
    driver.get(ADMIN_INDEX_URL)
    username_input = driver.find_element_by_id("username")
    pass_input = driver.find_element_by_id("password")
    login_btn = driver.find_element_by_id("login-button")
    username_input.send_keys(USERNAME)
    pass_input.send_keys(PASSWORD)
    login_btn.click()
    # print(driver.current_url)
    return driver


def admin_wrong_setup():
    driver = webdriver.Chrome()
    driver.get(ADMIN_INDEX_URL)
    username_input = driver.find_element_by_id("username")
    pass_input = driver.find_element_by_id("password")
    login_btn = driver.find_element_by_id("login-button")
    username_input.send_keys("illegal")
    pass_input.send_keys("illegal")
    login_btn.click()
    return driver


def main_setup():
    driver = webdriver.Chrome()
    driver.get(MAIN_INDEX_URL)
    username_input = driver.find_element_by_id("username")
    pass_input = driver.find_element_by_id("password")
    auth_btn = driver.find_element_by_id("auth-button")
    username_input.send_keys(USERNAME)
    pass_input.send_keys(PASSWORD)
    auth_btn.click()

    pj_list_select = Select(driver.find_element_by_id("project-list"))
    login_btn = driver.find_element_by_id("login-button")
    while not login_btn.is_enabled():
        time.sleep(1)
    pj_list_select.select_by_visible_text(GROUP_NAME)
    login_btn.click()
    return driver


def admin_user_btn_click(driver):
    users_btn = None
    while users_btn is None:
        try:
            time.sleep(1)
            users_btn = driver.find_element_by_xpath('//*[@id="navigation-panel"]/ul/li[2]/a')
        except Exception as e:
            print(e)
    users_btn.click()


def get_confirm_box_btns(driver):
    btns = []
    while len(btns) != 2:
        try:
            btns = driver.find_elements_by_css_selector(".bootstrap-dialog-footer-buttons > button")
            time.sleep(1)
        except Exception as e:
            print(e)
    return btns


def success_btn_click(driver):
    time.sleep(1)
    btn = None
    while btn is None:
        try:
            btn = driver.find_element_by_css_selector(".bootstrap-dialog-footer-buttons > button")
            time.sleep(1)
        except Exception as e:
            print(e)
    btn.click()


if __name__ == "__main__":
    main_setup()
