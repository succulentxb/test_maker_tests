from selenium import webdriver
import time

INDEX_URL = "https://www.qualtrics.com/"
LOGIN_URL = "https://login.qualtrics.com/login"
GRAPHICS_URL = "https://smeal.ca1.qualtrics.com/Q/GraphicsSection"

driver = webdriver.Chrome()
driver.get(INDEX_URL)

EMAIL = "minding@psu.edu"
PASSWORD = "xxx"


def login():
    driver.get(LOGIN_URL)
    time.sleep(1)
    login_btn = driver.find_element_by_css_selector("body > nav > div.top-section > div.top-nav.hidden-bl.hidden-xs.hidden-sm > div > div.custom-block > ul > li:nth-child(3) > a")
    login_btn.click()
    time.sleep(1)
    username_input = driver.find_element_by_id("UserName")
    pass_input = driver.find_element_by_id("UserPassword")
    username_input.send_keys(EMAIL)
    pass_input.send_keys(PASSWORD)
    submit_btn = driver.find_element_by_id("loginButton")
    submit_btn.click()
    time.sleep(1)


def get_imgs():
    driver.get(GRAPHICS_URL)
    jump_btns = driver.find_elements_by_css_selector("#LibraryFoldersContainer > div.content.upload-drop-area.ng-isolate-scope > div.elements-container.ng-scope.angular-ui-tree > div.pagination-footer.ng-scope > div > div:nth-child(3) > span")
    while len(jump_btns) == 0:
        time.sleep(1)
        jump_btns = driver.find_elements_by_css_selector(
            "#LibraryFoldersContainer > div.content.upload-drop-area.ng-isolate-scope > div.elements-container.ng-scope.angular-ui-tree > div.pagination-footer.ng-scope > div > div:nth-child(3) > span")
    for jump_btn in jump_btns:
        jump_btn.click()
        imgs = driver.find_elements_by_class_name("thumbnail-img")

