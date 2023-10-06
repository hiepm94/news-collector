import scrapy
import json

class ItemspiderHustSpider(scrapy.Spider):
    name = "itemspider_hust"
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(ItemspiderHustSpider, self).__init__(*args, **kwargs)
        with open('hustlink.json', 'r') as f:
            data = json.load(f)
            self.start_urls = [item['link'] for item in data]

    def parse(self, response):
        products = response.css('.panel-body')
        for product in products:
            # Truy xuất các thông tin bài viết
            title = product.css('.title::text').get()
            content = product.css('::text').getall()
            image_url = product.css('img::attr(src)').extract_first()

            # Loại bỏ các chuỗi rỗng (khoảng trắng) trong nội dung
            cleaned_content = [text.strip() for text in content if text.strip()]

            # Lấy URL hiện tại
            current_url = response.url

            # Kiểm tra nếu title và image_url khác null thì mới trả về dữ liệu
            if title is not None or image_url is not None:
                yield {
                    'title': title,
                    'content': cleaned_content,
                    'image_url': image_url,
                    'current_url': current_url,  # Thêm đường dẫn vào dữ liệu
                }
