import scrapy


class LinkspiderSpider(scrapy.Spider):
    name = "linkspider"
    allowed_domains = ["ulis.vnu.edu.vn"]
    start_urls = ["https://ulis.vnu.edu.vn/category/tin-tuc-va-su-kien/"]

    def parse(self, response):
        pass
