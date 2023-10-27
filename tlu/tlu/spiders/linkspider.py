import scrapy


class LinkspiderSpider(scrapy.Spider):
    name = "linkspider"
    allowed_domains = ["www.tlu.edu.vn"]
    start_urls = ["https://www.tlu.edu.vn/Tin-tuc-thong-bao"]

    def parse(self, response):
        pass
