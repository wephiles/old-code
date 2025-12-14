# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class DownloadimagesPipeline:
    fp = None

    def open_spider(self, spider):
        print('开始爬')
        self.fp = open('imagename.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(item['name'] + '\n')
        return item

    def close_spider(self, spider):
        self.fp.close()
        print('不爬了')


class DownloadimagesMySql(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            password='WarmDou_TS20866',
            db='runoob',
            charset='utf8')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('INSERT INTO sites (name, url) VALUES("%s", "%s")' % (item['name'], '1'))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

# END
