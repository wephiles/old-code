import scrapy
from images.items import ImagesItem


class TestSpider(scrapy.Spider):
    name = "test"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://desk.3gbizhi.com/deskMV/index_1.html"]

    def parse(self, response):
        li_list = response.xpath('//ul[@class="cl"]/li')
        for li in li_list:
            name = li.xpath('./div[@class="tips"]/a/text()').extract()
            name = ''.join(name)
            src = li.xpath('./a/@href')[0].extract()
            item = ImagesItem()
            item['name'] = name

            yield scrapy.Request(url=src,
                                 callback=self.parse_src,
                                 meta={'item': item})

    def parse_src(self, response):
        item = response.meta['item']
        real_src = response.xpath('//*[@id="showimg"]/a[4]/img/@src').extract_first()
        if real_src is not None:
            item['src'] = real_src
            yield item
# END
