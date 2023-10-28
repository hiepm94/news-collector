import scrapy
import json
import re
import dateparser
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urljoin

class ItemspiderHauSpider(scrapy.Spider):
    name = "itemspider_hau"
    allowed_domains = ["https://hau.edu.vn"]
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(ItemspiderHauSpider, self).__init__(*args, **kwargs)
        with open('haulink.json', 'r') as f:
            data = json.load(f)
            self.start_urls = [item['link'] for item in data][:50]

    def parse(self, response):
        title = response.css('#news-cate h1::text').get()
        title = re.sub(r'[\\"]|‘', '', title).strip()

        datetime_str = response.css('.pull-left::text').get()
        datetime_obj = dateparser.parse(datetime_str, languages=['vi'])

        content = response.css('div[class="post_content"] *::text').getall()
        cleaned_content = [text.strip() for text in content if text.strip()]
        cleaned_content = ' '.join(cleaned_content)
        cleaned_content = re.sub(r'[\\"]|‘', '', cleaned_content).strip()

        image_url = response.css('div[class="post_content"] img::attr(src)').extract_first()
        if image_url == None:
            image_url = response.css('.news_column .image-center img::attr(src)').extract_first()
        if image_url.startswith('/uploads'):
            image_url = "https://hau.edu.vn" + image_url
        image_url = response.urljoin(image_url)

        news_url = response.url
        yield {
            'title': title,
            'date': datetime_obj,
            'content': cleaned_content,
            'image_url': image_url,
            'news_url': news_url,
            'publication' : "hau",
        }
