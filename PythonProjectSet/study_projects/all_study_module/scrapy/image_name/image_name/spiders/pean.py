import scrapy


class PeanSpider(scrapy.Spider):
    name = 'pean'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://movie.douban.com/top250']

    # 生成一个通用的url模板 不可以改变的
    url_ = 'https://movie.douban.com/top250?start=%d&filter='
    page_num = 25

    def parse(self, response):
        text_ = response.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()').extract()
        print(text_)

        new_url = format(self.url_ % self.page_num)
        # 手动请求发送 callback回调函数 参数是专门用于数据解析
        if self.page_num <= 226:
            self.page_num += 26
            yield scrapy.Request(url=new_url, callback=self.parse)
        pass
