#!/usr/bin/env python3

import csv


class Saved(object):
    def __init__(self, path):
        self.path_file = path

    def write_file(self, data: list):

        csv_colums = data[0].keys()

        with open(self.path_file, "w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=csv_colums)
            writer.writeheader()

            for item in data:
                writer.writerow(item)

        print(f"[+] File {self.path_file} has been created.")
