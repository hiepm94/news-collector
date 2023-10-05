import scrapy
import json

class UlisitemSpider(scrapy.Spider):
    name = "ulisitem"
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(UlisitemSpider, self).__init__(*args, **kwargs)
        with open('link.json', 'r') as f:
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

    # Đọc dữ liệu từ tệp JSON
    with open('item.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Loại bỏ chuỗi rỗng (khoảng trắng) trong nội dung
    for item in data:
        item["content"] = [text.strip() for text in item["content"] if text.strip()]

    # Ghi dữ liệu đã được xử lý lại vào tệp JSON
    with open('item_cleaned.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)