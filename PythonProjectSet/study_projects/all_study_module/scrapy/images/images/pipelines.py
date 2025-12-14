# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy


# class ImagesPipeline:
#     def process_item(self, item, spider):
#         print(item)
#         return item


class ImagesPipeLine(ImagesPipeline):
    # 重写父类方法
    # 根据图片地址进行数据请求
    def get_media_requests(self, item, info):
        title = item['name'] + '.jpg'
        yield scrapy.Request(url=item['src'], meta={'title': title})

    # 指定图片存储路径 request是手动发送的请求对象
    def file_path(self, request, response=None, info=None):
        # image_name = request.url.split('/')[-1]  # 直接在网址中找文件名称
        image_name = request.meta['title']  # 下载的名称
        return image_name

    def item_completed(self, results, item, info):
        return item  # 返回给下一个即将使用的管道类

# END
