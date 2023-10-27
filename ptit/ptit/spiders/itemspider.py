import scrapy


class ItemspiderSpider(scrapy.Spider):
    name = "itemspider"
    allowed_domains = ["portal.ptit.edu.vn"]
    start_urls = ["https://portal.ptit.edu.vn/category/tin-tuc/"]

    def parse(self, response):
        pass
