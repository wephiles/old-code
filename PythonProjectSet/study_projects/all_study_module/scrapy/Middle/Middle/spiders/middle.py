import scrapy


class MiddleSpider(scrapy.Spider):
    name = "middle"
    allowed_domains = ["www.xxx.com"]
    start_urls = ["http://www.baidu.com"]

    def parse(self, response):
        page_text = response.text
        with open('../result/ip.html', 'w', encoding='utf-8') as fp:
            fp.write(page_text)

# END
