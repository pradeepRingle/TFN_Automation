from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.pool = 300
        self.wait = WebDriverWait(self.driver, self.timeout, self.pool)

        self.base_locators = {
            'app_loader': (By.XPATH, "//div[@class='app-loader']")
        }

        self.elem = "Element {} not found"

    def visit_url(self, url):
        self.driver.get(url)

    def wait_until_element_located(self, element):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located((element[0], element[1])))
        except ElementNotVisibleException:
            print(self.elem.format(element[1]))

    def wait_until_element_clickable(self, element):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                ec.element_to_be_clickable((element[0], element[1])))
        except ElementNotVisibleException:
            print(self.elem.format(element[1]))

    def wait_until_element_is_invisible(self, element):
        WebDriverWait(self.driver, self.timeout).until(
            ec.invisibility_of_element_located((element[0], element[1])))

    def check_if_element_exists(self, element):
        try:
            self.driver.find_element_by_xpath(element[1])
        except NoSuchElementException:
            return False
        return True

    def is_element_displayed(self, element):
        return self.wait_until_element_located(element).is_displayed()

    def is_element_enabled(self, element):
        return self.wait_until_element_located(element).is_enabled()

    def is_loading_started(self):
        return self.check_if_element_exists(self.base_locators.get('app_loader'))

    def is_loading_completed(self):
        if self.is_loading_started():
            self.wait_until_element_is_invisible(self.base_locators.get('app_loader'))
        else:
            assert True

    def send_tabs(self, n):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB * n)
        actions.perform()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def is_new_tab_opened(self):
        windows = self.driver.window_handles
        assert len(windows) > 1
        self.driver.switch_to.window(windows[1])

    def scroll_by_height(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
