#!/usr/bin/env python3

from scraper.checker import Checker
from scraper.parser import Parser
from selenium.webdriver.common.keys import Keys

import sys
import re
import time


class Scrape(object):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.get(self.url)

        self.list_companies = list()
        self.checker = Checker(self.browser)
        self.parser = Parser()

    def _get_total_pages(self):

        self.checker.check_element("search-results__pagination")

        elem_pagination = self.browser.find_element_by_xpath(
            "/html/body/main/div[1]/div/section/div[2]/nav/ol"
        )
        pages = elem_pagination.find_elements_by_tag_name("button")
        pages = [num.text for num in pages]

        return max(pages, key=int)

    def _get_url(self, i):

        elem_url = self.url.split("&")
        regex = re.compile("page=.")
        num_page = [string for string in elem_url if re.match(regex, string)][0]

        return self.url.replace(num_page, f"page={i}")

    def _get_companies(self, pages):
        try:
            print("[~] Press Ctrl + C to stop searching for information")
            for i in range(1, pages + 1):
                print(f"[~] Analyzing... {i}/{pages} \033[J", end="\r")
                url = self._get_url(str(i))
                self.browser.get(url)
                self.checker.check_element("search-results__result-item")

                for _ in range(0, 20):
                    self.browser.execute_script(
                        "window.scrollTo(0, window.scrollY + 200)"
                    )
                    companies = self.browser.find_elements_by_class_name(
                        "search-results__result-item"
                    )

                self.parser.companies_info_parse(companies)

        except KeyboardInterrupt:
            pass

        print(f"[+] {len(self.parser.data)} companies were captured.")
        return self.parser.data

    def main(self):

        pages = self._get_total_pages()
        companies = self._get_companies(int(pages))
        return companies
