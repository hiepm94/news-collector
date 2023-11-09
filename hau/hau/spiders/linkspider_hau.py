import scrapy

class LinkspiderHauSpider(scrapy.Spider):
    name = "linkspider_hau"
    allowed_domains = ["hau.edu.vn"]
    start_urls = ["https://hau.edu.vn/tin-tuc_c01/"]
    visited_urls = set()


    def parse(self, response):
        links = response.css('.caption a::attr(href)').getall()
        
        for link in links:
            if link in self.visited_urls:
                return
            self.visited_urls.add(link)
            if not link.startswith("https://hau.edu.vn"):
                link = "https://hau.edu.vn" + link

            yield {
                'link': link
            }
