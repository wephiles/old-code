import scrapy
from boss.items import BossItem


class PositionSpider(scrapy.Spider):
    name = "position"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.zhipin.com/web/geek/job?query=python&city=101030100&page=1"]

    url = 'https://www.zhipin.com/web/geek/job?query=python&city=101030100&page=%d'
    page_number = 2

    def parse(self, response):
        li_list = response.xpath('//ul[@class="job-list-box"]/li')
        for li in li_list:
            name = 'https://www.zhipin.com/' + \
                   li.xpath('./div[@class="job-card-body.clearfix"]/a/div/span/text()').extract()
            detail_url = li.xpath('div[@class="job-card-body.clearfix"]/a/@href').extract()
            item = BossItem()
            item['name'] = name
            # 对详情页发请求
            yield scrapy.Request(url=detail_url,
                                 callback=self.parse_detail,
                                 meta={'item': item})  # meta：请求传参 可以将item传给回调函数

        # 分页
        if self.page_number <= 10:
            new_url = format(self.url % self.page_number)
            self.page_number += 1
            yield scrapy.Request(url=new_url, callback=self.parse)

    def parse_detail(self, response):
        # 回调函数接受 item
        item = response.meta['item']

        job_description = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[1]/div[2]//text()').extract()
        job_description = ''.join(job_description)
        print(job_description)
        item['description'] = job_description
        yield item
# END
