import scrapy
from WangYi.items import WangyiItem
from selenium import webdriver


class NewsSpider(scrapy.Spider):
    name = "news"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://news.163.com/"]
    bro = None
    module_urls = []

    def __init__(self, **kwargs):
        """使用selenium 解析动态网页加载的数据"""
        # 实例化浏览器对象
        option = webdriver.ChromeOptions()
        option.add_argument('--ignore-certificate-errors')
        option.add_argument('--ignore-ssl-errors')
        option.add_experimental_option("excludeSwitches",
                                       ['enable-automation', 'enable-logging'])
        super().__init__(**kwargs)
        self.bro = webdriver.Chrome(executable_path='../chromedriver.exe',
                                    chrome_options=option)
        self.bro.implicitly_wait(20)

    def parse(self, response, *args, **kwargs):
        """解析响应数据response

        解析出需要的板块的网址
        :param response: 爬取到的网络信息 —— 响应对象
        :return: None
        """
        li_list = response.xpath('//*[@id="index2016_wrap"]'
                                 '/div[3]/div[2]/div[2]/div[2]/div/ul/li')
        name_list = ['国内', '国际']

        for li in li_list:
            module_name = li.xpath('./a/text()').extract_first()
            module_url = li.xpath('./a/@href').extract_first()
            if module_name in name_list:
                self.module_urls.append(module_url)
                yield scrapy.Request(url=module_url,
                                     callback=self.parse_module)

    def parse_module(self, response):
        """解析每一个模块下面的所有新闻的网址

        :param response: 爬取到的网络信息 —— 响应对象
        :return: None
        """
        div_list = response.xpath('/html/body/div/div[3]/div[3]/div[1]'
                                  '/div[1]/div/ul/li/div/div')
        print(len(div_list))

        for div in div_list:
            news_name = div.xpath('./div/div[1]/h3/a/text()').extract_first()

            news_url = div.xpath('./a/@href').extract_first()
            item = WangyiItem()
            item['news_name'] = news_name
            yield scrapy.Request(url=news_url,
                                 callback=self.parse_detail,
                                 meta={'item': item})

    def parse_detail(self, response):
        item = response.meta['item']
        news_detail = response.xpath('//*[@id="content"]'
                                     '/div[2]//text()').extract()
        news_detail = ''.join(news_detail)
        news_detail = news_detail.replace(' ', '').replace('\n', '')
        item['news_content'] = news_detail
        yield item

    def closed(self, spider):
        self.bro.close()
        self.bro.quit()

# END
