# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QuanPipeline:
    # 有两个item 怎么区分是哪个item呢？
    def process_item(self, item, spider):
        if item.__class__.__name__ == 'DetailItem':
            print(item['webpage_url'])
        else:
            print(item['image_title'], item['image_url'])
        return item
