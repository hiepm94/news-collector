import scrapy


class LinkspiderSpider(scrapy.Spider):
    name = "linkspider_utc"
    allowed_domains = ["www.utc.edu.vn"]
    start_urls = ["https://www.utc.edu.vn/tin-tuc"]
    visited_urls = set()


    def parse(self, response):
        links = response.css('.lastest-news .i-title a::attr(href)').getall()
        for link in links:
            if link in self.visited_urls:
                return
            self.visited_urls.add(link)
            yield {
                'link': link
            }
