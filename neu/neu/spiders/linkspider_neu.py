import scrapy


class LinkspiderNeuSpider(scrapy.Spider):
    name = "linkspider_neu"
    allowed_domains = ["neu.edu.vn"]
    start_urls = ["https://neu.edu.vn/vi/tin-tuc-moi-nhat"]

    def parse(self, response):
        links = response.css('div.article-content a::attr(href)').getall()
        for link in links:
            if link in self.visited_urls:
                return
            self.visited_urls.add(link)
            yield {
                'link': link
            }