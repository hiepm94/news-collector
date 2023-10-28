import scrapy
import json
import re
import dateparser
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urljoin

class ItemspiderUebSpider(scrapy.Spider):
    name = "itemspider_ueb"
    allowed_domains = ["ueb.vnu.edu.vn"]
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(ItemspiderUebSpider, self).__init__(*args, **kwargs)
        with open('ueblink.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.start_urls = [item['link'] for item in data][:50]

    def parse(self, response):
        title = response.css('.about-intro-title::text').get()
        title = re.sub(r'[\\"]|‘', '', title).strip()

        datetime_str =  response.css('span.spanTimer').get().replace('<span class="spanTimer">\r\n                            <i class="icon-time"></i>\r\n','').replace('\r\n                        </span>','')
        datetime_obj = dateparser.parse(datetime_str, languages=['vi'])

        content = response.css('div[class="about-detail posmb-5 pt-3"] *::text').getall()
        cleaned_content = [text.strip() for text in content if text.strip()]
        cleaned_content = ' '.join(cleaned_content)
        cleaned_content = re.sub(r'[\\"]|‘', '', cleaned_content).strip()

        image_url = response.css('div[class="about-detail posmb-5 pt-3"] img::attr(src)').extract_first()
        if image_url == None:
            image_url = response.css('.news_column .image-center img::attr(src)').extract_first()
        if image_url.startswith('/uploads'):
            image_url = "https://www.utc.edu.vn" + image_url
        image_url = response.urljoin(image_url)

        news_url = response.url
        yield {
            'title': title,
            'date': datetime_obj,
            'content': cleaned_content,
            'image_url': image_url,
            'news_url': news_url,
            'publication' : "ueb",
        }
