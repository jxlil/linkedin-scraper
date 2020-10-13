#!/usr/bin/env python3


class Parser(object):
    def __init__(self):
        self.data = list()

    def verify_info(self, item: str) -> str:
        return item if item else "Unknown"

    def companies_info_parse(self, companies_info: list):

        for companie in companies_info:
            info = dict.fromkeys(["Name", "URL", "Employees", "Country", "Sector"], "")

            try:
                info["Name"] = companie.find_element_by_xpath(
                    "div[2]/div/div/div/article/section[1]/div[1]/dl/dt/a"
                ).text

                info["URL"] = companie.find_element_by_xpath(
                    "div[2]/div/div/div/article/section[1]/div[1]/dl/dt/a"
                ).get_attribute("href")

                info["Employees"] = companie.find_element_by_xpath(
                    "div[2]/div/div/div/article/section[1]/div[1]/dl/dd[3]/ul/li[2]"
                ).text

                info["Country"] = companie.find_element_by_xpath(
                    "div[2]/div/div/div/article/section[1]/div[1]/dl/dd[3]/ul/li[3]"
                ).text

                info["Sector"] = companie.find_element_by_xpath(
                    "div[2]/div/div/div/article/section[1]/div[1]/dl/dd[3]/ul/li[1]"
                ).text

            except:

                for key, value in info.items():
                    info[key] = self.verify_info(value)

            self.data.append(info)

