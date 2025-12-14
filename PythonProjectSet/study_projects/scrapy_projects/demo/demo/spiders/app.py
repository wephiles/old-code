# -*- coding: utf-8 -*-
# @CreateTime : 2024/6/14 014 0:00
# @Author : wephiles@20866
# @IDE : PyCharm
# @ProjectName : demo
# @FileName : demo/app.py
# @Description : This is description of this script.
# @Interpreter : python 3.10
# @Motto : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles
# @Copyright : © 2024 wephiles. All rights reserved.

import scrapy


# class QuotesSpider(scrapy.Spider):
#
# name = "quotes"
#
# def start_requests(self):
#     urls = [
#         'http://quotes.toscrape.com/page/1/',
#         'http://quotes.toscrape.com/page/2/',
#     ]
#     for url in urls:
#         yield scrapy.Request(url=url, callback=self.parse)
#
# def parse(self, response):
#     page = response.url.split("/")[-2]
#     filename = 'quotes-%s.html' % page
#     with open(filename, 'wb') as f:
#         f.write(response.body)
#     self.log('Saved file %s' % filename)


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        start_urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        file_name = "quotes-{}.html".format(page)
        with open(file_name, 'wb') as fp:
            fp.write(response.body)
        self.log('Saved file: {}'.format(file_name))

# --END--
