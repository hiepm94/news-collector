import scrapy


class LinkspiderSpider(scrapy.Spider):
    name = "linkspider"
    allowed_domains = ["www.haui.edu.vn"]
    start_urls = ["https://www.haui.edu.vn/vn/tin-tuc"]

    def parse(self, response):
        pass
