import scrapy
import json

class UlisitemSpider(scrapy.Spider):
    name = "ulisitem"
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(UlisitemSpider, self).__init__(*args, **kwargs)
        with open('item.json', 'r') as f:
            data = json.load(f)
            self.start_urls = [item['link'] for item in data]

    def parse(self, response):
        products = response.css('.post-content')
        for product in products:
            # Truy xuất các thông tin bài viết
            title = product.css('h2.title::text').get()
            content = product.css('p::text').getall()

            # Trả về dữ liệu
            yield {
                'title': title,
                'content': content,
            }
