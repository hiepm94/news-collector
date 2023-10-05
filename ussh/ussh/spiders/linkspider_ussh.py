import scrapy
from ussh.itemloaders import ChocolateProductLoader
from ussh.items import UsshItem 

class LinkspiderUsshSpider(scrapy.Spider):
    name = "linkspider_ussh"
    allowed_domains = ["ussh.vnu.edu.vn"]
    start_urls = ["https://ussh.vnu.edu.vn/vi/news/"]

    def parse(self, response):
        links = response.css('.news_column .panel-default a::attr(href)').getall()

        for link in links:
            # Kiểm tra nếu đường dẫn không bắt đầu bằng "https://ussh.vnu.edu.vn"
            if not link.startswith("https://ussh.vnu.edu.vn"):
                # Nếu không, nối đường dẫn với "https://ussh.vnu.edu.vn"
                link = "https://ussh.vnu.edu.vn" + link
            
            yield {
                'link': link  # Trả về đường link trong dạng một dictionary
            }
