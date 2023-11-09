import scrapy
import json
import re
import dateparser

class ItemspiderSpider(scrapy.Spider):
    name = "itemspider"
    allowed_domains = ["ajc.hcma.vn"]
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(ItemspiderSpider, self).__init__(*args, **kwargs)
        with open('ajclink.json', 'r') as f:
            data = json.load(f)
            self.start_urls = [item['link'] for item in data][:50]

    def parse(self, response):
        title = response.css('.tieu-de::text').get()
        title = re.sub(r'[\\"]|‘', '', title).strip()

        # Update the selector to match the correct element containing the datetime
        datetime_str = response.css('div[class="col-xs-6 none-padding sukien"]').get().replace('<div class=\"col-xs-6 none-padding sukien\">\r\n                    <p>\r\n                        <img src=\"/Publishing/images/date%20_ct.svg\">\r\n                        ','').replace('\r\n                    </p>\r\n                </div>','')
        datetime_obj = dateparser.parse(datetime_str, languages=['vi'])

        content = response.css('.img-class *::text').getall()
        cleaned_content = [text.strip() for text in content if text.strip()]
        cleaned_content = ' '.join(cleaned_content)
        cleaned_content = re.sub(r'[\\"]|‘', '', cleaned_content).strip()

        image_url = response.css('.img-class img::attr(src)').extract_first()
        if image_url == None:
            image_url = response.css('.news_column .image-center img::attr(src)').extract_first()
        if image_url and image_url.startswith('/uploads'):
            image_url = "https://hau.edu.vn" + image_url
        image_url = response.urljoin(image_url)

        news_url = response.url
        yield {
            'title': title,
            'date': datetime_obj,
            'content': cleaned_content,
            'image_url': image_url,
            'news_url': news_url,
            'publication': "ajc",
        }
