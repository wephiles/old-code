import scrapy
from qiutu_project.items import QiutuProjectItem

class QiutuBaikeSpider(scrapy.Spider):
    name = 'qiutu_baike'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://movie.douban.com/top250']


    # def parse(self, response):
    #     # 解析电影名称 + 评价
    #     all_data = []
    #     list_get_name = response.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()').extract()
    #     list_get_talk = response.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[2]/span/text()').extract()
    #     print('Got all data!!!')
    #     # 持久化存储： 基于终端指令：只可以将parse方法的返回值存储到本地的文本文件中，不可以存数据库
    #     # 即parse方法必须有一个返回值: 简洁高效便捷 但是局限性较大，只能存在指定后缀的文本文档中
    #
    #     for i in range(0, 25):
    #         dic_ = {
    #             'name': list_get_name[i],
    #             'talk': list_get_talk[i]
    #         }
    #         all_data.append(dic_)
    #
    #     # 持久化存储： 基于管道 要更加常用
    #     return all_data
    #     pass

    # 持久化存储： 基于管道 要更加常用
    def parse(self, response):
        # 解析电影名称 + 评价
        # all_data = []
        list_get_name = response.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()').extract()
        list_get_talk = response.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[2]/span/text()').extract()
        print('Got all data!!!')
        # 持久化存储： 基于终端指令：只可以将parse方法的返回值存储到本地的文本文件中，不可以存数据库
        # 即parse方法必须有一个返回值: 简洁高效便捷 但是局限性较大，只能存在指定后缀的文本文档中

        for i in range(0, 25):
            talk = list_get_talk[i]
            name = list_get_name[i]
            item = QiutuProjectItem()
            item['name'] = name
            item['content'] = talk
            # 将item提交给管道
            yield item
        pass
