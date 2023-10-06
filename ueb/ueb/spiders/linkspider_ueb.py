import scrapy
from urllib.parse import urljoin

class LinkspiderUebSpider(scrapy.Spider):
    name = "linkspider_ueb"
    allowed_domains = ["ueb.vnu.edu.vn"]
    start_urls = ["https://ueb.vnu.edu.vn/Tin-Tuc/TIN-TUC-CHUNG/1659"]

    def parse(self, response):
        links = response.css('.mt-3 .font-weight-bold::attr(href)').getall()

        # Kiểm tra và nối đường dẫn nếu chúng không bắt đầu bằng "https://ueb.vnu.edu.vn/"
        links = [urljoin(response.url, link) if not link.startswith("https://ueb.vnu.edu.vn/") else link for link in links]

        for link in links:
            yield {
                'link': link  # Trả về đường link trong dạng một dictionary
            }

        # next_page = response.css('a.next.page-numbers::attr(href)').get()

        # if next_page is not None:
        #     full_next_page_url = urljoin(response.url, next_page)
        #     yield response.follow(full_next_page_url, callback=self.parse)
