# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse
from time import sleep


class WangyiDownloaderMiddleware:

    # def process_request(self, request, spider):
    #     return request

    def process_response(self, request, response, spider):
        bro = spider.bro
        if request.url in spider.module_urls:
            sleep(1)
            bro.get(request.url)
            sleep(1)
            page_text = bro.page_source
            new_response = HtmlResponse(url=request.url,
                                        body=page_text,
                                        encoding='utf-8',
                                        request=request)
            return new_response
        return response

    # def process_exception(self, request, exception, spider):
    #     return request

