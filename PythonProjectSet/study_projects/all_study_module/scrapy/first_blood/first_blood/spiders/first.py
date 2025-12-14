import scrapy


class FirstSpider(scrapy.Spider):  # Spider是scrapy里面的类，是所有爬虫类的父类
    name = 'first'  # 爬虫文件名称 我们创建的：就是爬虫源文件的唯一标识

    # 允许的域名：用来限定start_urls中的哪些域名能请求发送,一般不用
    # allowed_domains = ['www.baidu.com']

    # 起始url列表，该列表存放的url会被scrapy自动进行请求发送
    start_urls = ['https://www.baidu.com/', 'https://www.csdn.net/']



    def parse(self, response):
        # 用作于数据解析，response表示请求成功后对应的响应对象
        print(response)
        pass
