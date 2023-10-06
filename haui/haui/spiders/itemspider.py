import scrapy


class ItemspiderSpider(scrapy.Spider):
    name = "itemspider"
    allowed_domains = ["www.haui.edu.vn"]
    start_urls = ["https://www.haui.edu.vn/vn/tin-tuc"]

    def parse(self, response):
        pass
