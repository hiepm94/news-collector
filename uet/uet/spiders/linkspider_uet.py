import scrapy


class LinkspiderUetSpider(scrapy.Spider):
    name = "linkspider_uet"
    allowed_domains = ["uet.vnu.edu.vn"]
    start_urls = ["https://uet.vnu.edu.vn/category/tin-tuc/"]

    def parse(self, response):
        links = response.css('.main-color-1-hover::attr(href)').getall()

        for link in links:
            yield {
                'link': link  # Trả về đường link trong dạng một dictionary
            }

        # next_page = response.css('[rel="next"] ::attr(href)').get()

        # if next_page is not None:
        #     next_page_url = next_page
        #     yield response.follow(next_page_url, callback=self.parse)
