import scrapy
import json
import re
import dateparser
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urljoin


class ItemspiderUetSpider(scrapy.Spider):
    name = "itemspider"
    allowed_domains = ["uet.vnu.edu.vn"]
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(ItemspiderUetSpider, self).__init__(*args, **kwargs)
        with open('uetlink.json', 'r') as f:
            data = json.load(f)
            self.start_urls = [item['link'] for item in data][:50]

    def parse(self, response):
        title = response.css('.single-content-title::text').get()
        title = re.sub(r'[\\"]|‘', '', title).strip()

        datetime_str = response.css('div.item-meta.single-post-meta.content-pad span:nth-child(2)::text').get()
        datetime_obj = dateparser.parse(datetime_str, languages=['vi'])

        content = response.css('div[class="single-post-content-text content-pad"] *::text').getall()
        cleaned_content = [text.strip() for text in content if text.strip()]
        cleaned_content = ' '.join(cleaned_content)
        cleaned_content = re.sub(r'[\\"]|‘', '', cleaned_content).strip()

        image_url = response.css('div[class="single-post-content-text content-pad"] img::attr(src)').extract_first()
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
            'publication' : "uet",
        }



# class ItemspiderUetSpider(scrapy.Spider):
#     name = "itemspider_uet"
#     start_urls = []

#     def __init__(self, *args, **kwargs):
#         super(ItemspiderUetSpider, self).__init__(*args, **kwargs)
#         with open('uetlink.json', 'r') as f:
#             data = json.load(f)
#             self.start_urls = [item['link'] for item in data]

#     def parse(self, response):
#         products = response.css('.col-md-9')
#         for product in products:
#             # Truy xuất các thông tin bài viết
#             title = product.css('.single-content-title::text').get()
#             content = product.css('::text').getall()
#             image_url = product.css('img::attr(src)').extract_first()

#             # Loại bỏ các chuỗi rỗng (khoảng trắng) trong nội dung
#             cleaned_content = [text.strip() for text in content if text.strip()]

#             # Lấy URL hiện tại
#             news_url = response.url

#             # Trả về dữ liệu
#             yield {
#                 'title': title,
#                 'content': cleaned_content,
#                 'image_url' : image_url,
#                 'news_url': news_url,  # Thêm đường dẫn vào dữ liệu
#             }
