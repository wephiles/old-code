import scrapy
from embarrassment.items import EmbarrassmentItem


class EmbarrassSpider(scrapy.Spider):
    name = "embarrass"

    # allowed_domains = ["author.baidu.com"]
    start_urls = ["http://author.baidu.com/home/1549062383207647"]

    # def parse(self, response):
    #     # 解析作者名称 段子内容
    #     # div_list = response.xpath('*//div[@class="feed-item"]')
    #     div_list = [0, 1, 2, 3, 4, 5]
    #     dic_ = {}
    #     all_data = []
    #     if len(div_list) == 0:
    #         print('Can not find element!')
    #     for div in div_list:
    #         # number = div.xpath('./div//div[@class="s-card-body"]'
    #         #                    '/div[@class="sfi-dynamic-subscript"]'
    #         #                    '/span/text()').extract_first()
    #         # # 也可以将[0]去掉 写.extract_first() 如果返回的列表只有一个列表元素时才可使用
    #         # # selector 对象调用extract()
    #         # title = div.xpath('./div/div[@class="s-card"]//div[@class="text-title"]/pre/text()').extract()
    #         number = '123456'
    #         title = '计算机哈哈好'
    #         dic_ = {
    #             'number': number,
    #             'title': title
    #         }
    #         all_data.append(dic_)
    #         number += str(div)
    #         title += str(div)
    #     print('OK')
    #     return all_data

    def parse(self, response):
        div_list = [0, 1, 2, 3, 4, 5]
        if len(div_list) == 0:
            print('Can not find element!')
        for div in div_list:
            # number = div.xpath('./div//div[@class="s-card-body"]'
            #                    '/div[@class="sfi-dynamic-subscript"]'
            #                    '/span/text()').extract_first()
            # # 也可以将[0]去掉 写.extract_first() 如果返回的列表只有一个列表元素时才可使用
            # # selector 对象调用extract()
            # title = div.xpath('./div/div[@class="s-card"]//div[@class="text-title"]/pre/text()').extract()
            number = '123456'
            title = '计算机哈哈好'

            item = EmbarrassmentItem()
            item['number'] = number
            item['title'] = title

            number = number + str(div)
            title = title + str(div)

            yield item  # 提交管道

