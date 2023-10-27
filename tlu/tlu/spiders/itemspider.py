import scrapy


class ItemspiderSpider(scrapy.Spider):
    name = "itemspider"
    allowed_domains = ["www.tlu.edu.vn"]
    start_urls = ["https://www.tlu.edu.vn/Tin-tuc-thong-bao"]

    def parse(self, response):
        pass
