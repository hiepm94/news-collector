import scrapy


class LinkspiderSpider(scrapy.Spider):
    name = "linkspider"
    allowed_domains = ["www.haui.edu.vn"]
    start_urls = ["https://www.haui.edu.vn/vn/tin-tuc"]
    visited_urls = set()

    def parse(self, response):
        links = response.css('.entry-title a::attr(href)').getall()
        for link in links:
            if link in self.visited_urls:
                return
            self.visited_urls.add(link)
            if not link.startswith("https://www.haui.edu.vn"):
                link = "https://www.haui.edu.vn" + link
            yield {
                'link': link
            }

