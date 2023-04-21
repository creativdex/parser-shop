import re
import logging
from bs4 import BeautifulSoup
from schemas import InputSchemas, GuidIrl
from selenium import webdriver
from pydantic import parse_obj_as


class Parser:
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s"
    )

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless=new")
        self.options.add_argument("--disable-images")
        self.options.add_experimental_option("detach", True)

    async def __aenter__(self):
        self.driver = webdriver.Remote(
            command_executor="http://192.168.243.20:4444",
            options=self.options,
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()
        if exc_val:
            logging.info(f"Ошибка: {exc_type}")
            raise

    async def get_page(self, url):
        self.driver.get(url)
        page = self.driver.page_source
        return page

    async def get_spec_dns(self, page):
        soup = BeautifulSoup(page, "html.parser")
        find_block = soup.find_all(
            attrs=[
                "product-characteristics__spec-title",
                "product-characteristics__spec-value",
            ]
        )
        spec_list = [i.getText() for i in find_block]
        result = [
            {"key": spec_list[i], "value": spec_list[i + 1]}
            for i in range(0, len(spec_list), 2)
        ]
        logging.info(f"Парсинг завершен: {self.driver.current_url}")
        return result

    async def guid_url(self, input: InputSchemas):
        dicts = [{"guid": k, "url": v} for k, v in input.__root__.items()]
        return parse_obj_as(GuidIrl, *dicts)

    async def check_url_dns(self, url: str):
        if re.search("characteristics", url):
            return url
        else:
            if url[-1] == "/":
                url = url + "characteristics/"
                return url
            else:
                url = url + "/characteristics/"
                return url
