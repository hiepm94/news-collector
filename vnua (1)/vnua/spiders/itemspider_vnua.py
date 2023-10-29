import scrapy
import json
import re
import dateparser
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ItemspiderVnuaSpider(scrapy.Spider):
    name = "itemspider_vnua"
    allowed_domains = ["vnua.edu.vn"]
    start_urls = ["https://vnua.edu.vn/tin-tuc-su-kien"]

    def __init__(self, *args, **kwargs):
        super(ItemspiderVnuaSpider, self).__init__(*args, **kwargs)
        try:
            with open('vnualink.json', 'r') as f:
                data = json.load(f)
                self.start_urls = [item['link'] for item in data][:50]
        except Exception as e:
            self.log("Error loading start URLs from vnualink.json: %s" % str(e))

    def parse(self, response):
        posts = response.css('div[class="box-post box-post-list"]')

        for post in posts:
            title = post.css('h3.post-title a::text').get()
            title = re.sub(r'[\\"]|‘', '', title).strip()
            title = re.sub(r'\s+', ' ', title).strip()

            datetime_str = post.css('.lbPublishedDate::text').get().replace('Cập nhật lúc ', '')
            datetime_obj = dateparser.parse(datetime_str, languages=['vi'])

            content = post.css('.post-short-content *::text').getall()
            cleaned_content = ' '.join(text.strip() for text in content if text.strip())
            cleaned_content = re.sub(r'[\\"]|‘', '', cleaned_content).strip()

            image_url = post.css('img::attr(src)').extract_first()
            if image_url and image_url.startswith('/uploads'):
                image_url = "https://www.vnua.edu.vn" + image_url
            image_url = response.urljoin(image_url)

            news_url = response.urljoin(post.css('h3.post-title a::attr(href)').get())

            yield {
                'title': title,
                'date': datetime_obj,
                'content': cleaned_content,
                'image_url': image_url,
                'news_url': news_url,
                'publication': "vnua",
            }
