import scrapy
from downloadimages.items import DownloadimagesItem


class PracticeSpider(scrapy.Spider):
    name = "practice"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.3gbizhi.com/tag/bizhi/1.html"]

    # 生成一个通用的url模板 (不可改变)
    url = 'https://www.3gbizhi.com/tag/bizhi/%d.html'
    page_number = 2

    def parse(self, response):
        try:
            li_list = response.xpath('/html/body/div[4]/ul/li')
        except Exception as e:
            print(e)
        else:
            for li in li_list:
                img_name_single_list = li.xpath('./div[@class="tips"]/a/text()').extract()
                img_name = ' '.join(img_name_single_list)
                item = DownloadimagesItem()
                item['name'] = img_name
                yield item

            if self.page_number <= 11:
                new_url = format(self.url % self.page_number)
                self.page_number += 1
                # 手动请求发送 callback 回调函数是专门用作于数据解析
                yield scrapy.Request(url=new_url, callback=self.parse)

# END
