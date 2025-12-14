# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline

# 下面这个用不了，需要重新定义一个
# class ImageGetPipeline:
#     def process_item(self, item, spider):
#         return item


class ImgPipeLine(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 更具图片地址进行图片数据的请求

        yield scrapy.Request(item['src'])  # 不需要callback

    def file_path(self, request, response=None, info=None, *, item=None):
        # 指定图片存储的路劲
        img_name = request.url.split('/')[-1]
        return img_name

    def item_completed(self, results, item, info):
        # 返回给下一个即将被执行的管道类
        return item
