import scrapy


class LinkspiderSpider(scrapy.Spider):
    name = "linkspider"
    allowed_domains = ["www1.napa.vn"]
    start_urls = ["https://www1.napa.vn/blog/category/tin-tuc/tin-hoat-dong"]
    visited_urls = set()


    def parse(self, response):
        links = response.css('.entry-title a::attr(href)').getall()
        
        for link in links:
            # if link in self.visited_urls:
            #     return
            # self.visited_urls.add(link)
            # if not link.startswith("www1.napa.vn"):
            #     link = "www1.napa.vn" + link

            yield {
                'link': link
            }
