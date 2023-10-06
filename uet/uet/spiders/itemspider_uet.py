import scrapy
import json

class ItemspiderUetSpider(scrapy.Spider):
    name = "itemspider_uet"
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(ItemspiderUetSpider, self).__init__(*args, **kwargs)
        with open('uetlink.json', 'r') as f:
            data = json.load(f)
            self.start_urls = [item['link'] for item in data]

    def parse(self, response):
        products = response.css('.col-md-9')
        for product in products:
            # Truy xuất các thông tin bài viết
            title = product.css('.single-content-title::text').get()
            content = product.css('::text').getall()
            image_url = product.css('img::attr(src)').extract_first()

            # Loại bỏ các chuỗi rỗng (khoảng trắng) trong nội dung
            cleaned_content = [text.strip() for text in content if text.strip()]

            # Lấy URL hiện tại
            news_url = response.url

            # Trả về dữ liệu
            yield {
                'title': title,
                'content': cleaned_content,
                'image_url' : image_url,
                'news_url': news_url,  # Thêm đường dẫn vào dữ liệu
            }
