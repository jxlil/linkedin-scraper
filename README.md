# Linkedin Scraper
Created for the automatic collection of companies in Linkedin Sales

## Installation

### Prerequisites
+ Python3
    ```bash
    sudo apt install python3 python3-pip
    ```

+ [Chrome Browser](https://www.google.com/chrome/)
+ [Chromedriver](https://chromedriver.chromium.org/)

    > NOTE:
        The *chromedriver* version should be compatible with the version of your Chrome browser

### Install

```
git clone https://github.com/jxlil/linkedin-scraper
cd linkedin-scraper

pip3 install -r requirements.txt --user
```

## Usage

```
usage: scraper.py [-h] -u URL -d DRIVER [-o OUTPUT] [-v]

Business scraper on Linkedin

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     set URL
  -d DRIVER, --driver DRIVER
                        Set path to chromedriver
  -o OUTPUT, --output OUTPUT
                        Set output file name
  -v, --version         show program's version number and exit

```

## Example

1. Edit the `config.yml` file with your credentials to login to linkedin:

    ```bash
    # config.yml

    email: example@domain.com
    password: 123456
    ```

2. Determine the URL to scrape:

    To determine the URL, enter the [Sales Navigator](https://www.linkedin.com/sales/search/) and then enter a keyword to search for companies or use filters. When filtering the companies of your interest, copy the url of the browser. Example:

    ```
    https://www.linkedin.com/sales/search/company?keywords=apple&page=1&searchSessionId=Nh%2BNeGnhTyKubjmZPyS4%2BQ%3D%3D
    ```

3. Start scraping information:

    To start execute the following command, determined the URL of your interest, the path to the chromedriver and the name of the file where you will save the information.

    ```
    python3 bin/scraper.py -u https://www.linkedin.com/sales/search/company?keywords=apple&page=1&searchSessionId=Nh%2BNeGnhTyKubjmZPyS4%2BQ%3D%3D -d '~/chromedriver' -o example.csv
    ```

4. When finished, the file `example.csv` will have been created that will contain the information:

    - Name of the company
    - Linkedin profile
    - Number of employees
    - Country of the company
    - Business sector


---
    

