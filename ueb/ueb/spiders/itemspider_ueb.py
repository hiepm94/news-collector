import scrapy
import json

class ItemspiderUebSpider(scrapy.Spider):
    name = "itemspider_ueb"
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(ItemspiderUebSpider, self).__init__(*args, **kwargs)
        with open('ueblink.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.start_urls = [item['link'] for item in data]

    def parse(self, response):
        products = response.css('div.container')
        for product in products:
            # Truy xuất các thông tin bài viết
            title = product.css('.about-intro-title::text').get()
            content = product.css('p::text').getall()
            image_url = product.css('img::attr(src)').extract_first()

            # Loại bỏ các chuỗi rỗng (khoảng trắng) trong nội dung
            cleaned_content = [text.strip() for text in content if text.strip()]

            # Lấy URL hiện tại
            news_url = response.url

            # Trả về dữ liệu
            if title is not None and image_url is not None:
                yield {
                    'title': title,
                    'content': cleaned_content,
                    'image_url': image_url,
                    'news_url': news_url,  # Thêm đường dẫn vào dữ liệu
                }