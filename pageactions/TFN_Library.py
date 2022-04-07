import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from pageactions.BasePage import BasePage
from selenium.webdriver.common.keys import Keys
import string
import random


class TFN_Library(BasePage):
    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver
        )

    def visit_url(self, url):
        self.driver.get(url)

    def verify_duplicate_message(self, label):
        message = self.wait_until_element_clickable(label).text
        assert message == 'Duplicate Check: The record already exists.'

    def verify_mandatory_message(self, label):
        message = self.wait_until_element_clickable(label).text
        assert message == 'You might have unsaved changes, are you sure you want to leave?'

    def verify_pop_up_message(self, label):
        message = self.wait_until_element_clickable(label).text
        assert message == "Write the number of TFNs to add and press [ENTER]"

    def send_keyboard_keys(self, label, keys):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.wait_until_element_located(label))
        time.sleep(1)
        self.driver.execute_script("arguments[0].setAttribute('style', 'border:2px solid red; background:pink')",
                                   self.wait_until_element_located(label))
        time.sleep(1)
        self.wait_until_element_clickable(label).send_keys(keys)

    def send_keyboard_edit_keys(self, label, keys):
        time.sleep(5)
        self.wait_until_element_located(label).clear()
        self.wait_until_element_clickable(label).send_keys(keys)

    def get_text(self, label):
        return self.wait_until_element_located(label).text

    def click_event(self, label):
        self.is_loading_completed()
        self.wait_until_element_clickable(label).click()
        self.is_loading_completed()

    def double_click_using_action_chains(self, label):
        self.wait_until_element_clickable(label)
        action = ActionChains(self.driver)
        action.move_to_element(self.wait_until_element_located(label))
        action.double_click().perform()
        self.is_loading_completed()

    def single_click_using_action_chains(self, label):
        self.wait_until_element_clickable(label)
        action = ActionChains(self.driver)
        action.move_to_element(self.wait_until_element_located(label))
        action.click().perform()
        self.is_loading_completed()

    def auto_search_cross_button(self, label):
        self.wait_until_element_clickable(label)
        self.wait_until_element_located(label).click()

    def auto_search_result_verify(self, label, label1, test):
        self.is_loading_completed()
        self.wait_until_element_clickable(label)
        verify = self.wait_until_element_located(label1).text
        assert str(test).lower() in str(verify).lower()

    def auto_search_no_result(self, label, label1):
        self.wait_until_element_clickable(label)
        verify = self.wait_until_element_located(label1).text
        assert verify == 'No Results Found'

    def file_upload(self, label, filepath):
        self.driver.find_element_by_xpath(label[1]).send_keys(filepath)

    @staticmethod
    def get_random_alpha_numeric_string(size):
        # initializing size of string
        n = size
        # using random.choices()
        # generating random strings
        res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase +
                                     string.digits, k=n))
        return str(res)
