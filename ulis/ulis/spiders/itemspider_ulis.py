import scrapy
import json
import re
import dateparser
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ItemspiderSpider(scrapy.Spider):
    name = "itemspider_ulis"
    allowed_domains = ["ulis.vnu.edu.vn"]
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(ItemspiderSpider, self).__init__(*args, **kwargs)
        with open('ulislink.json', 'r') as f:
            data = json.load(f)
            self.start_urls = [item['link'] for item in data][:50]

    def parse(self, response):
        title = response.css('.post-content .title::text').get()
        title = re.sub(r'[\\"]|‘', '', title).strip()

        datetime_str = response.css('.index-post-date::text').get()
        parts = datetime_str.split()
        if len(parts) == 3:
            new_datetime_str = f"{parts[1]} {parts[0]},{parts[2]}"
        else:
            new_datetime_str = datetime_str

        def custom_date_parser(date_str):
            try:
                return dateparser.parse(date_str, languages=['vi'])
            except Exception as e:
                return None

        datetime_obj = custom_date_parser(new_datetime_str)

        content = response.css('div[id="dslc-theme-content-inner"] *::text').getall()
        cleaned_content = [text.strip() for text in content if text.strip()]
        cleaned_content = ' '.join(cleaned_content)
        cleaned_content = re.sub(r'[\\"]|‘', '', cleaned_content).strip()

        image_url = response.css('div[id="dslc-theme-content-inner"] img::attr(src)').extract_first()
        if image_url == None:
            image_url = response.css('.news_column .image-center img::attr(src)').extract_first()
        if image_url and image_url.startswith('/uploads'):
            image_url = response.urljoin(image_url)

        news_url = response.url
        yield {
            'title': title,
            'date': new_datetime_str,
            'datetime_obj': datetime_obj,
            'content': cleaned_content,
            'image_url': image_url,
            'news_url': news_url,
            'publication': "ulis",
        }


    # # Đọc dữ liệu từ tệp JSON
    # with open('item.json', 'r', encoding='utf-8') as json_file:
    #     data = json.load(json_file)

    # # Loại bỏ chuỗi rỗng (khoảng trắng) trong nội dung
    # for item in data:
    #     item["content"] = [text.strip() for text in item["content"] if text.strip()]

    # # Ghi dữ liệu đã được xử lý lại vào tệp JSON
    # with open('item_cleaned.json', 'w', encoding='utf-8') as json_file:
    #     json.dump(data, json_file, indent=4, ensure_ascii=False)