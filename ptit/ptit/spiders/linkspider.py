import scrapy


class LinkspiderSpider(scrapy.Spider):
    name = "linkspider"
    allowed_domains = ["portal.ptit.edu.vn"]
    start_urls = ["https://portal.ptit.edu.vn/category/tin-tuc/"]

    def parse(self, response):
        links = response.css('h2.entry-title a::attr(href)').getall()
        for link in links:
            if link in self.visited_urls:
                return
            self.visited_urls.add(link)
            yield {
                'link': link
            }
