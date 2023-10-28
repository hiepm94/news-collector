import scrapy


class LinkspiderSpider(scrapy.Spider):
    name = "linkspider_utc"
    allowed_domains = ["www.utc.edu.vn"]
    start_urls = ["https://ueb.vnu.edu.vn/Tin-Tuc/tin-tuc-chung"]
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
