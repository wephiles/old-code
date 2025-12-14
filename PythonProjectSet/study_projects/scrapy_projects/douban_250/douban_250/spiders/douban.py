import scrapy
from douban_250.items import Douban250Item


class DoubanSpider(scrapy.Spider):
    name = "douban"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://movie.douban.com/top250?start=0&filter="]

    # def parse(self, response):
    #     # 解析 title + 名言
    #     li_list = response.xpath('//ol[@class="grid_view"]/li')
    #     # 存储解析到的所有数据
    #     all_data = []
    #     for li in li_list:
    #         # xpath返回的元素一定是列表 但是列表中的元素一定是selector类型的对象
    #         # .extract()可以将selector对象中存储的字符串提取出来
    #         # title = li.xpath('.//div[@class="hd"]/a/span[1]/text()')[0].extract().strip()
    #
    #         # 这条语句等价于title = li.xpath('.//div[@class="hd"]/a/span[1]/text()')[0].extract().strip()
    #         # 当你确保返回数据只有一个元素 你就可以用extract_first
    #         title = li.xpath('.//div[@class="hd"]/a/span[1]/text()').extract_first().strip()
    #
    #         # xpath使用//text()可以获得列表 可能有多个元素
    #         # 列表调用extract，表示将列表中每个selector对象中data对应的字符串提取出来
    #         quotes = ''.join(li.xpath('.//div[@class="bd"]/div[@class="star"]//text()').extract()).strip().replace('\n',
    #                                                                                                                ' ').replace("\t",
    #                                                                                                                             " ")
    #         dict_save = {
    #             'title': title,
    #             'quotes': quotes
    #         }
    #         all_data.append(dict_save)
    #         # print(title, quotes)
    #     return all_data
    def parse(self, response):
        # 解析 title + 名言
        li_list = response.xpath('//ol[@class="grid_view"]/li')
        # 存储解析到的所有数据
        all_data = []
        for li in li_list:
            # xpath返回的元素一定是列表 但是列表中的元素一定是selector类型的对象
            # .extract()可以将selector对象中存储的字符串提取出来
            # title = li.xpath('.//div[@class="hd"]/a/span[1]/text()')[0].extract().strip()

            # 这条语句等价于title = li.xpath('.//div[@class="hd"]/a/span[1]/text()')[0].extract().strip()
            # 当你确保返回数据只有一个元素 你就可以用extract_first
            title = li.xpath('.//div[@class="hd"]/a/span[1]/text()').extract_first().strip()

            # xpath使用//text()可以获得列表 可能有多个元素
            # 列表调用extract，表示将列表中每个selector对象中data对应的字符串提取出来
            quotes = ''.join(li.xpath('.//div[@class="bd"]/div[@class="star"]//text()').extract()).strip().replace('\n',
                                                                                                                   ' ').replace("\t", "")
            item = Douban250Item()
            item['title'] = title
            item['quotes'] = quotes

            # 将item提交给管道
            yield item
