import json
import re
import dateparser
import scrapy
from scrapy.http import TextResponse

class ItemspiderUsshSpider(scrapy.Spider):
    name = "itemspider_ussh"
    allowed_domains = ['ussh.vnu.edu.vn']

    def __init__(self, *args, **kwargs):
        super(ItemspiderUsshSpider, self).__init__(*args, **kwargs)
        with open('usshlink.json', 'r') as f:
            data = json.load(f)
            self.start_urls = [item['link'] for item in data][:50]

    def parse(self, response):
        title = response.css('.title::text').get()
        datetime_str = response.css('.h5::text').get()
        datetime_obj = dateparser.parse(datetime_str, languages=['vi'])
        content = response.css('div.news_column.panel.panel-default *::text').getall()
        cleaned_content = [text.strip() for text in content if text.strip()]
        cleaned_content = ' '.join(cleaned_content).strip()
        cleaned_content = re.sub(r'https?://\S+', '', cleaned_content)
        image_url = response.css('img.img-thumbnail::attr(src)').extract_first()
        if image_url is None:
            image_url = response.css('.news_column .image-center img::attr(src)').extract_first()

        if image_url and image_url.startswith('/uploads'):
            image_url = "https://ussh.vnu.edu.vn" + image_url
        news_url = response.url

        yield {
            'title': title,
            'date': datetime_obj,
            'content': cleaned_content,
            'image_url': image_url,
            'news_url': news_url,
            'publication': "ussh",
        }
