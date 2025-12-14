import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from time import sleep
from Quan.items import QuanItem, DetailItem
import random


class TestSpider(CrawlSpider):
    name = "test"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://pic.netbian.com/"]
    link = LinkExtractor(allow=r'/index_\d+.html')
    link_detail = LinkExtractor(allow=r'/tupian/\d+.html')  # 获取图片地址
    rules = (
        # Rule 规则解析器 ： 将链接提取器提取到的链接进行指定规则的解析操作
        # 这个解析操作是由 callback（）指定的
        Rule(
            link,
            callback="parse_item",
            follow=False),
        # follow 为 True 可以将链接提取器作用到链接提取器所获取到的页面中
        Rule(
            link_detail,
            callback="parse_detail",
            follow=False
            # 如果不需要再利用正则爬取详情页信息 则不需要写follow=FALSE
        )
    )

    # 如下两个方法是不可以实现请求传参的
    # 无法将数据存到同一个item中 可以一次存储到两个item中
    def parse_item(self, response):
        item = {}
        sleep(1)
        # li_list = response.xpath('//*[@id="main"]/div[3]/ul/li')
        # print(len(li_list))
        # for li in li_list:
        for i in range(0, 20):
            # sleep(1)
            # image_name = li.xpath(r'./a/b/text()').extract_first()
            # image_url = li.xpath(r'./a/span/img/@src').extract_first()

            item = QuanItem()
            # item['image_title'] = image_name
            # item['image_url'] = image_url
            item['image_title'] = '这是' + str(random.randint(1, 50))
            item['image_url'] = 'url' + str(random.randint(1, 50))
            yield item
        return item

    def parse_detail(self, response):
        item = DetailItem()
        item['webpage_url'] = 'he he' + str(random.randint(1, 50))
        yield item
        return item

# END
