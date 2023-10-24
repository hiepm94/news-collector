import scrapy

class LinkspiderHustSpider(scrapy.Spider):
    name = "linkspider_hust"
    allowed_domains = ["www.hust.edu.vn"]
    start_urls = ["https://www.hust.edu.vn/vi/news/"]
    visited_urls = set()

    def parse(self, response):
        links = response.css('a.show::attr(href)').getall()
        for link in links:
            if link in self.visited_urls:
                return
            self.visited_urls.add(link)
            yield {
                'link': link
            }
