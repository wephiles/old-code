# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse
from time import sleep


class NewsDownloaderMiddleware:

    # def process_request(self, request, spider):
    #     return None

    def process_response(self, request, response, spider):
        bro = spider.bro
        # 每拦截一次 响应一次
        # spider 表示爬虫对象
        # 拦截五大板块的响应数据 对数据进行改动 改成符合需求的响应对象
        # 本函数可以兰街到所有响应对象
        # 挑选出指定的响应对象 进行改动 —— 通过url
        if request.url in spider.module_urls:
            # 五大板块对应的响应对象
            # 针对定位到的对象进行改动
            # 实例化一个新的响应对象（动态加载出的） 替代旧的响应对象
            # 如何获取动态加载的数据？？？—— 基于 selenium
            bro.get(request.url)  # 发送请求 对五个板块对应的url请求发送
            sleep(3)
            page_text = bro.page_source
            # 包含了动态加载的数据
            new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
            return new_response
        return response

    # def process_exception(self, request, exception, spider):
    #     pass

