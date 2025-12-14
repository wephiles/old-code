import scrapy


# scrapy.Spider:所有爬虫类的父类
class FirstSpiderSpider(scrapy.Spider):
    # 爬虫文件名称 就是爬虫源文件的唯一标识
    name = "first_spider"

    # # 允许的域名 用来限制start_urls列表中哪些url可以进行请求发送
    # # 一般情况下allowed_domains不使用
    # allowed_domains = ["www.baidu.com"]

    # 起始url列表:该列表中存放的url会被scrapy自动进行请求的发送
    start_urls = ["https://www.baidu.com", "https://www.sogou.com/"]

    # 用于数据解析 response参数表示请求成功后对应的响应对象
    def parse(self, response):
        print(response)
