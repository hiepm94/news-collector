import scrapy


class LinkspiderHauSpider(scrapy.Spider):
    name = "linkspider_hau"
    allowed_domains = ["hau.edu.vn"]
    start_urls = ["https://hau.edu.vn/tin-tuc_c01/"]

    def parse(self, response):
        links = response.css('.caption a::attr(href)').getall()

        for link in links:
            # Kiểm tra nếu đường dẫn không bắt đầu bằng "https://ussh.vnu.edu.vn"
            if not link.startswith("https://hau.edu.vn"):
                # Nếu không, nối đường dẫn với "https://ussh.vnu.edu.vn"
                link = "https://hau.edu.vn" + link
            
            yield {
                'link': link  # Trả về đường link trong dạng một dictionary
            }
