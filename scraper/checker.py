#!/usr/bin/env python3

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

MIN_WAITING_TIME = 10
MAX_WAITING_TIME = 60

import sys


class Checker(object):
    def __init__(self, browser):
        self.browser = browser

    def _close_browser(self):
        print("[!] Closing the browser...")
        self.browser.close()

    def check_element(self, element):
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, element))
            WebDriverWait(self.browser, MAX_WAITING_TIME).until(element_present)

        except TimeoutException:
            print("[x] Could not load page")
            self._close_browser()
            sys.exit(1)

