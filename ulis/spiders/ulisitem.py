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
        titles = response.css('h2.title::text').getall()
        content = response.css('p::text').getall()
        

        articles = []

        for title, paragraph in zip(titles, content):
            article = {"title": title, "content": paragraph}
            articles.append(article)

        # Trả về từng bài báo dưới dạng danh sách động
        for article in articles:
            yield article