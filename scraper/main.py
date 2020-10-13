#!/usr/bin/env python3

from selenium import webdriver
from scraper.login import Login
from scraper.scrape import Scrape
from scraper.saved import Saved
from scraper.banner import Banner


class Init(object):
    def __init__(self, args):

        self.banner = Banner()
        self.banner.print_banner()

        self.browser = webdriver.Chrome(args.driver)
        self.login()

        companies = self.scrape_information(args.url)
        self.saved_information(args.output, companies)

    def login(self):
        login = Login(self.browser)
        login.main()

    def scrape_information(self, url):
        scraper = Scrape(self.browser, url)
        return scraper.main()

    def saved_information(self, path, companies):
        saved = Saved(path)
        saved.write_file(companies)

