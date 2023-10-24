import scrapy
import json
import re
import dateparser
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class ItemspiderHustSpider(scrapy.Spider):
    name = "itemspider_hust"
    allowed_domains = ['hust.edu.vn']
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(ItemspiderHustSpider, self).__init__(*args, **kwargs)
        with open('hustlink.json', 'r') as f:
            data = json.load(f)
            self.start_urls = [item['link'] for item in data][:50]

    def parse(self, response):
        title = response.css('h1.title::text').get()
        title = re.sub(r'[\\"]|‘', '', title).strip()

        datetime_str = response.css('span[class="h5"]::text').get()
        datetime_obj = dateparser.parse(datetime_str, languages=['vi'])

        content = response.css('#news-bodyhtml *::text').getall()
        cleaned_content = [text.strip() for text in content if text.strip()]
        cleaned_content = ' '.join(cleaned_content)
        cleaned_content = re.sub(r'[\\"]|‘', '', cleaned_content).strip()

        image_url = response.css('img.img-thumbnail::attr(src)').extract_first()
        if image_url == None:
            image_url = response.css('.news_column .image-center img::attr(src)').extract_first()
        if image_url.startswith('/uploads'):
            image_url = "https://www.hust.edu.vn" + image_url
        news_url = response.url
        yield {
            'title': title,
            'date': datetime_obj,
            'content': cleaned_content,
            'image_url': image_url,
            'news_url': news_url,
        }