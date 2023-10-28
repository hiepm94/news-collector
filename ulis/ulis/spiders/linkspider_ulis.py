import scrapy


class LinkspiderSpider(scrapy.Spider):
    name = "linkspider"
    allowed_domains = ["ulis.vnu.edu.vn"]
    start_urls = ["https://ulis.vnu.edu.vn/category/tin-tuc-va-su-kien/"]
    visited_urls = set()

    def parse(self, response):
        links = response.css('h2.title a::attr(href)').getall()

        for link in links:
            if link in self.visited_urls:
                return
            self.visited_urls.add(link)
            yield {
                'link': link
            }

        # next_page = response.css('a.next.page-numbers::attr(href)').get()

        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)