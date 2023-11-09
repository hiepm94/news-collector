import scrapy


class LinkspiderSpider(scrapy.Spider):
    name = "linkspider"
    allowed_domains = ["www.hvnh.edu.vn"]
    start_urls = ["https://www.hvnh.edu.vn/hvnh/vi/box/ban-tin-hoc-vien-ngan-hang"]
    visited_urls = set()


    def parse(self, response):
        links = response.css('div[class="col-xs-12 col-sm-4 col-md-4 col-lg-4"] a::attr(href)').getall()
        
        for link in links:
            if link in self.visited_urls:
                return
            self.visited_urls.add(link)
            if not link.startswith("https://www.hvnh.edu.vn"):
                link = "https://www.hvnh.edu.vn" + link

            yield {
                'link': link
            }

