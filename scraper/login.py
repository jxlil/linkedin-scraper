#!/usr/bin/env python3

import yaml
import time


class Login(object):
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(
            "https://www.linkedin.com/login/es?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
        )

    def get_credentials(self):

        with open("config.yml", "r") as f:
            credentials = yaml.load(f, Loader=yaml.FullLoader)

        return credentials["email"], credentials["password"]

    def _write_email(self, email):
        email_elem = self.browser.find_element_by_css_selector("#username")
        email_elem.clear()
        email_elem.send_keys(email)

    def _write_passw(self, password):
        passw_elem = self.browser.find_element_by_css_selector("#password")
        passw_elem.clear()
        passw_elem.send_keys(password)

    def click_login_button(self):
        login_button = self.browser.find_element_by_css_selector(
            "#app__container > main > div:nth-child(2) > form > div.login__form_action_container > button"
        )
        login_button.click()

    def verify_login(self):

        try:
            # If there is a captcha you must log in manually
            _ = self.browser.find_element_by_xpath("/html/body/div/main/iframe")

            print("[!] Linkedin has detected that it uses an automation script")
            input("[~] Please log in manually and when finished press ENTER")

        except Exception:
            pass

    def main(self):

        email, password = self.get_credentials()
        self._write_email(email)
        self._write_passw(password)
        self.click_login_button()
        self.verify_login()
