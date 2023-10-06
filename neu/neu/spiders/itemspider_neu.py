import scrapy


class ItemspiderNeuSpider(scrapy.Spider):
    name = "itemspider_neu"
    allowed_domains = ["neu.edu.vn"]
    start_urls = ["https://neu.edu.vn/vi/tin-tuc-moi-nhat"]

    def parse(self, response):
        pass
