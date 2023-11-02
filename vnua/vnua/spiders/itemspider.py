import scrapy


class ItemspiderSpider(scrapy.Spider):
    name = "itemspider"
    allowed_domains = ["vnua.edu.vn"]
    start_urls = ["https://vnua.edu.vn/tin-tuc-su-kien"]

    def parse(self, response):
        pass
