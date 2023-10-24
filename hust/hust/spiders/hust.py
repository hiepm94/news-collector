import scrapy
import json
import re
from datetime import datetime
import dateparser
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class HustSpider(CrawlSpider):
    name = "hust"
    allowed_domains = ['hust.edu.vn']
    start_urls = ['https://www.hust.edu.vn/vi/']
    visited_urls = set()

# https://www.hust.edu.vn/vi/news/hoat-dong-chung/
# https://www.hust.edu.vn/vi/news/cong-tac-dang-va-doan-the/
# https://www.hust.edu.vn/vi/news/tuyen-sinh-dao-tao-cong-tac-sinh-vien/
# https://www.hust.edu.vn/vi/news/khoa-hoc-cong-nghe-dmst/
# https://www.hust.edu.vn/vi/news/hop-tac-doi-ngoai-truyen-thong/
# https://www.hust.edu.vn/vi/news/kiem-dinh-xep-hang/
# https://www.hust.edu.vn/vi/news/to-chuc-nhan-su-tuyen-dung/

# ['tin-tuc-su-kien', 'hoat-dong-chung', 
# 'cong-tac-dang-va-doan-the', 'tuyen-sinh-dao-tao-cong-tac-sinh-vien', 
# 'khoa-hoc-cong-nghe-dmst', 'hop-tac-doi-ngoai-truyen-thong', 
# 'kiem-dinh-xep-hang', 'to-chuc-nhan-su-tuyen-dung']

# https://www.hust.edu.vn/vi/news/hoat-dong-chung/
# https://www.hust.edu.vn/vi/news/hoat-dong-chung/gs-hoang-chi-bao-chia-se-nhung-cau-chuyen-ve-bac-ho-voi-gioi-tri-thuc-khoa-hoc-ky-thuat-va-dai-hoc-bach-khoa-ha-noi-654878.html    
    rules = (
        Rule(LinkExtractor(allow='news',
                        deny=['hoat-dong-chung', 'tin-tuc-su-kien',
                                'cong-tac-dang-va-doan-the', 'tuyen-sinh-dao-tao-cong-tac-sinh-vien',
                                'khoa-hoc-cong-nghe-dmst', 'hop-tac-doi-ngoai-truyen-thong',
                                'kiem-dinh-xep-hang', 'to-chuc-nhan-su-tuyen-dung'])),
        Rule(LinkExtractor(allow=['hoat-dong-chung']), callback='parse_item'))


    def parse_item(self, response):
        if response.url in self.visited_urls:
            return

        self.visited_urls.add(response.url)
        
        title = response.css('h1.title::text').get()
        title = re.sub(r'[\\"]|‘', '', title).strip()

        datetime_str = response.css('span[class="h5"]::text').get()
        datetime_obj = dateparser.parse(datetime_str, languages=['vi'])

        content = response.css('#news-bodyhtml *::text').getall()
        cleaned_content = [text.strip() for text in content if text.strip()]
        cleaned_content = ' '.join(cleaned_content)
        cleaned_content = re.sub(r'[\\"]|‘', '', cleaned_content).strip()

        image_url = response.css('img.img-thumbnail::attr(src)').extract_first()
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