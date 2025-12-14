import scrapy
from image_get.items import ImageGetItem


class ImageMaterialSpider(scrapy.Spider):
    name = 'image_material'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')  # 拿到所有的存放图片的div下面
        for div in div_list:
            # 注意： 在解析的时候使用伪属性
            src = 'https:' + div.xpath('./div/a/img/@src2').extract_first()
            # print(src)
            # 把图片地址提交到item
            item = ImageGetItem()
            item['src'] = src
            yield item
        pass
