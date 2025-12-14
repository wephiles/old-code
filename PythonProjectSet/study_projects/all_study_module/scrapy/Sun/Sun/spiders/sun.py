import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from Sun.items import SunItem


class SunSpider(RedisCrawlSpider):
    name = "sun"
    # allowed_domains = ["www.xxx.com"]
    # start_urls = ["http://www.xxx.com/"]

    # 可以被共享的调度器队列的名称
    start_urls = 'https://pic.netbian.com/'
    rules = (
        Rule(LinkExtractor(allow=r"/index_\d+.html"),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        item = {}
        li_list = response.xpath('//*[@id="main"]/div[3]/ul/li')
        # print(len(li_list))
        for li in li_list:
            # sleep(1)
            image_name = li.xpath(r'./a/b/text()').extract_first()
            image_url = li.xpath(r'./a/span/img/@src').extract_first()

            item = SunItem()
            item['image_title'] = image_name
            item['image_url'] = image_url
            # item['image_title'] = '这是' + str(random.randint(1, 50))
            # item['image_url'] = 'url' + str(random.randint(1, 50))
            yield item
        return item
