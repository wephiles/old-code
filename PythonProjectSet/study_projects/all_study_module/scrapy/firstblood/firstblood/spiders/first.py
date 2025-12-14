import scrapy


class FirstSpider(scrapy.Spider):
    name = "first"  # 爬虫文件名称--爬虫源文件的唯一标识 不能重复
    # allowed_domains = ["www.baidu.com"]  # 允许域名 用来限制起始url列表哪些url可以被请求 常被注释

    # 起始url列表 该列表中存放的列表会被scrapy自动请求发送
    start_urls = ["http://www.baidu.com/", "https://www.runoob.com"]

    # 用于数据解析 response表示请求成功对应的响应对象
    def parse(self, response):
        print(response)

