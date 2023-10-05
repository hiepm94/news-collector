import scrapy


class ItemspiderSpider(scrapy.Spider):
    name = "itemspider"
    allowed_domains = ["ulis.vnu.edu.vn"]
    start_urls = ["https://ulis.vnu.edu.vn/category/tin-tuc-va-su-kien/"]

    def parse(self, response):
        pass
