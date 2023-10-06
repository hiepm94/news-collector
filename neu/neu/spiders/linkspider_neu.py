import scrapy


class LinkspiderNeuSpider(scrapy.Spider):
    name = "linkspider_neu"
    allowed_domains = ["neu.edu.vn"]
    start_urls = ["https://neu.edu.vn/vi/tin-tuc-moi-nhat"]

    def parse(self, response):
        # Sử dụng CSS Selector để lấy tất cả các thẻ <article>
        articles = response.css('div.articles article')

        # Lặp qua các thẻ article và trích xuất liên kết
        for article in articles:
            link = article.css('a::attr(href)').extract_first()

            yield {
                'link': link  # Trả về đường dẫn trong dạng một dictionary
            }