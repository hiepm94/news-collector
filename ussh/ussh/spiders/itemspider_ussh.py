import scrapy
import json

class ItemspiderUsshSpider(scrapy.Spider):
    name = "itemspider_ussh"
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(ItemspiderUsshSpider, self).__init__(*args, **kwargs)
        with open('usshlink.json', 'r') as f:
            data = json.load(f)
            self.start_urls = [item['link'] for item in data]

    def parse(self, response):
        products = response.css('div.panel-body')
        for product in products:
            # Truy xuất các thông tin bài viết
            title = product.css('.title::text').get()
            content = product.css('::text').getall()
            image_urls = product.css('img::attr(src)').extract_first()

            # Kiểm tra nếu đường dẫn không bắt đầu bằng "https://ussh.vnu.edu.vn"
            if not image_urls.startswith("https://ussh.vnu.edu.vn"):
                # Nếu không, nối đường dẫn với "https://ussh.vnu.edu.vn"
                image_urls = "https://ussh.vnu.edu.vn" + image_urls

            # Loại bỏ các chuỗi rỗng (khoảng trắng) trong nội dung
            cleaned_content = [text.strip() for text in content if text.strip()]        

            # Trả về dữ liệu
            yield {
                'title': title,
                'content': cleaned_content,
                'image_url': image_urls,
            }
