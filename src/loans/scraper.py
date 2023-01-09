import time
from pathlib import Path

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from .constants import BASE_URL, SCRAPED_URL


class Scraper:
    """
    Scraper to get all loan data from https://www.eib.org/en/projects/loans/index.htm
    """

    def _get_driver(self):
        driver_path = str(
            Path(__file__).resolve().parent.parent.parent / "requirements/chromedriver"
        )

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--window-size=1920,1200")

        driver = webdriver.Chrome(options=options, executable_path=driver_path)
        driver.get(SCRAPED_URL)
        time.sleep(10)

        loans_per_page_button = driver.find_element(
            By.XPATH, '//*[@id="show-entries"]/option[4]'
        )
        loans_per_page_button.click()
        time.sleep(10)
        return driver

    def get_loans(self):
        driver = self._get_driver()
        soup = BeautifulSoup(driver.page_source, "html.parser")

        loan_list = []

        elements = soup.find_all("article")
        for index, article in enumerate(elements):
            # don't get the first row and  the last one
            if 0 < index < 101:
                loan = {}

                title = article.find("h3", {"class": "row-title"})
                loan["title"] = title.find("a").text
                loan["loan_url"] = BASE_URL + title.find("a")["href"]
                loan["signature_date"] = article.find(
                    "span", {"class": "row-date"}
                ).text

                all_divs = article.find_all("div")
                loan["signed_amount"] = all_divs[-1].text

                x = article.find_all("div", {"class": "row-tags"})
                for el in x:
                    country_a_tag = el.find("a")
                    if country_a_tag:
                        loan["country"] = country_a_tag.text
                        loan["country_url"] = BASE_URL + country_a_tag["href"]
                    else:
                        loan["sector"] = el.span.text
                loan_list.append(loan)
        driver.quit()
        return loan_list
