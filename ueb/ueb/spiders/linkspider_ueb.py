import scrapy
from urllib.parse import urljoin

class LinkspiderUebSpider(scrapy.Spider):
    name = "linkspider_ueb"
    allowed_domains = ["ueb.vnu.edu.vn"]
    start_urls = ["https://ueb.vnu.edu.vn/Tin-Tuc/TIN-TUC-CHUNG/1659", "https://ueb.vnu.edu.vn/Tin-Tuc/su-kien/1657"]
    visited_urls = set()


    def parse(self, response):
        links = response.css('.mt-3 .font-weight-bold::attr(href)').getall()

        for link in links:
            if link in self.visited_urls:
                return
            self.visited_urls.add(link)
            if not link.startswith("https://ueb.vnu.edu.vn"):
                link = "https://ueb.vnu.edu.vn" + link
            yield {
                'link': link
            }

        # next_page = response.css('a.next.page-numbers::attr(href)').get()

        # if next_page is not None:
        #     full_next_page_url = urljoin(response.url, next_page)
        #     yield response.follow(full_next_page_url, callback=self.parse)
