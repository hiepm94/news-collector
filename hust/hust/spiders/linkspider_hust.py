import scrapy


class LinkspiderHustSpider(scrapy.Spider):
    name = "linkspider_hust"
    allowed_domains = ["www.hust.edu.vn"]
    start_urls = ["https://www.hust.edu.vn/vi/news/"]

    def parse(self, response):
        links = response.css('a.show::attr(href)').getall()

        for link in links:
            yield {
                'link': link  # Trả về đường link trong dạng một dictionary
            }
