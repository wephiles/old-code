import scrapy
from boss_information.items import BossInformationItem


class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse_detail(self, response):
        # 回调函数接受item：
        # item = response.meta['item']
        job_desc = response.xpath('//*[@id="link-report"]/span[1]/span/text()').extract()
        # job_desc = ''.join(job_desc)
        # for i in job_desc:
        #     item['detail'] = i
        print(job_desc)
        pass

    def parse(self, response):
        # job_name_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()').extract()
        # url_detail_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/@href').extract()
        # # print(job_name_list)
        # for i in range(0, len(job_name_list)):
        #     item = BossInformationItem()
        #     item['name'] = job_name_list
        #     for items in range(0, len(url_detail_list)):
        #         # 请求传参，参数是一个字典，就可以将item传递给对应的回调函数
        #         yield scrapy.Request(url=url_detail_list[items], callback=self.parse_detail, meta={'item': item})
        li_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for li in li_list:
            item = BossInformationItem()
            name = li.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract()
            item['name'] = name
            # print(name)
            url_detail = li.xpath('./div/div[2]/div[1]/a/@href').extract()
            yield scrapy.Request(url=url_detail, callback=self.parse_detail, meta={'item': item})
        pass
