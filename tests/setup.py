from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

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


if __name__ == "__main__":
    main_setup()
