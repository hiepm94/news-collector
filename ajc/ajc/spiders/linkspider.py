import scrapy


class LinkspiderSpider(scrapy.Spider):
    name = "linkspider"
    allowed_domains = ["ajc.hcma.vn"]
    start_urls = ["https://ajc.hcma.vn/tintuc/pages/tin-tuc-su-kien.aspx"]
    visited_urls = set()

    def parse(self, response):
        links = response.css('.p-tieude a::attr(href)').getall()
        
        for link in links:
            if link in self.visited_urls:
                return
            self.visited_urls.add(link)
            if not link.startswith("https://ajc.hcma.vn/tintuc/pages/tin-tuc-su-kien.aspx"):
                link = "https://ajc.hcma.vn/tintuc/pages/tin-tuc-su-kien.aspx" + link

            yield {
                'link': link
            }
