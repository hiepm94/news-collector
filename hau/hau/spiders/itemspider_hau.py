import scrapy
import json

class ItemspiderHauSpider(scrapy.Spider):
    name = "itemspider_hau"
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(ItemspiderHauSpider, self).__init__(*args, **kwargs)
        with open('haulink.json', 'r') as f:
            data = json.load(f)
            self.start_urls = [item['link'] for item in data]

    def parse(self, response):
        products = response.css('article.thumbnail-news-view')
        for product in products:
            # Truy xuất các thông tin bài viết
            title = product.css('h1::text').get()
            content = product.css('::text').getall()
            image_url = product.css('.post_content img::attr(src)').extract_first()

            # Kiểm tra và xử lý đường dẫn ảnh
            if image_url and not image_url.startswith("https://hau.edu.vn"):
                # Nếu đường dẫn không bắt đầu bằng "https://hau.edu.vn",
                # thì nối đường dẫn với "https://hau.edu.vn"
                image_url = "https://hau.edu.vn" + image_url

            # Loại bỏ các chuỗi rỗng (khoảng trắng) trong nội dung
            cleaned_content = [text.strip() for text in content if text.strip()]

            # Lấy URL hiện tại
            news_url = response.url

            # Trả về dữ liệu
            yield {
                'title': title,
                'content': cleaned_content,
                'image_url': image_url,
                'news_url': news_url,  # Thêm đường dẫn vào dữ liệu
            }
