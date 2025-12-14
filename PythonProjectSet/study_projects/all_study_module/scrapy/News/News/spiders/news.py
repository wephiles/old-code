import scrapy
from selenium import webdriver
from News.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = "news"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://news.163.com/"]
    module_urls = []  # 存储详情页url

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])

        # 实例化一个浏览器对象
        self.bro = webdriver.Chrome(executable_path='../chromedriver.exe',
                                    chrome_options=options)
        self.bro.implicitly_wait(20)

    def parse(self, response):
        a_list = [2, 3]
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[3]/div[2]/div[2]/div[2]/div/ul/li')
        for index in a_list:
            module_url = li_list[index].xpath('./a/@href').extract_first()
            if module_url is not None:
                self.module_urls.append(module_url)
        for url in self.module_urls:
            yield scrapy.Request(url=url,
                                 callback=self.parse_module)

    def parse_module(self, response):
        """解析每一个板块页面中新闻标题

        再解析新闻详情页的url
        """
        div_list = response.xpath('/html/body/div/div[3]/div[3]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div[@class="na_detail"]/div[@class="news_title"]'
                              '/h3/a/text()').extract_first()

            news_detail_url = div.xpath('./div[@class="na_detail"]'
                                        '/div[@class="news_title"]/h3/a/@href').extract_first()

            print(title, news_detail_url)

            item = NewsItem()

            item['title'] = title
            yield scrapy.Request(url=news_detail_url,
                                 callback=self.parse_detail,
                                 meta={'item': item})

    def parse_detail(self, response):
        item = response.meta['item']
        content = response.xpath('//*[@id="content"]/div[2]//text()').extract()
        content = ''.join(content)

        print(content)

        item['content'] = content
        yield item

    # 爬虫结束 重写关闭函数
    def closed(self, spider):
        self.bro.quit()

# END
