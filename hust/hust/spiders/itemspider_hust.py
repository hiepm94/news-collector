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
            content = product.css('#news-bodyhtml::text').getall()
            image_url = product.css('img::attr(src)').extract_first()

            # Loại bỏ các chuỗi rỗng (khoảng trắng) trong nội dung
            cleaned_content = [text.strip() for text in content if text.strip()]


            # Trả về dữ liệu
            yield {
                'title': title,
                'content': cleaned_content,
                'image_url' : image_url,
            }