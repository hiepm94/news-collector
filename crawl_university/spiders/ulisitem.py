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
        # Sử dụng CSS selector để lấy tiêu đề và nội dung
        titles = response.css('h2.title::text').getall()
        content = response.css('div.single-content::text').getall()
        
        articles = []

        # Lặp qua các tiêu đề và nội dung để tạo danh sách bài báo
        for title, paragraph in zip(titles, content):
            article = {"title": title.strip(), "content": paragraph.strip()}
            articles.append(article)

        # Trả về từng bài báo dưới dạng danh sách động
        for article in articles:
            yield article
