import scrapy

class LinkspiderSpider(scrapy.Spider):
    name = "linkspider"
    allowed_domains = ["tlu.edu.vn"]
    start_urls = ["https://www.tlu.edu.vn/Tin-tuc-thong-bao"]
    visited_urls = set()

    def parse(self, response):
        links = response.css('.related-title .ng-binding::attr(href)').getall()
        urls_image = response.css('.img-responsive::attr(src)').getall()

        for link, url_image in zip(links, urls_image):
            if (link, url_image) in self.visited_urls:
                continue
            self.visited_urls.add((link, url_image))
            yield {
                'link': link,
                'url_image': url_image,
            }
