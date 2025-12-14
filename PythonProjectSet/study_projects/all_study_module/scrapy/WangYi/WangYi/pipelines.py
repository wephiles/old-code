# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class WangyiPipeline:
    fp = None

    def open_spider(self, spider):
        print('给爷爬！')
        self.fp = open('../result/news.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        print('正在存储到文件······')
        self.fp.write(item['news_name'])
        self.fp.write(': ')
        self.fp.write(item['news_content'])
        self.fp.write('\n')
        print('存储文件完成！')
        return item

    def close_spider(self, spider):
        self.fp.close()
        print('爬完了，爷！')


class MySQLPipeline(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        print('正在打开数据库')
        self.conn = pymysql.Connect(host='localhost',
                                    port=3306,
                                    user='root',
                                    password='WarmDou_TS20866',
                                    db='runoob',
                                    charset='utf8')

    def process_item(self, item, spider):
        print('正在保存到数据库······')
        self.cursor = self.conn.cursor()
        self.cursor.execute('INSERT INTO sites (name, url) '
                            'VALUES ("%s", "%s")'
                            % (item['news_name'], '我就是个占位的，内容太长了'))
        ...

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
        print('数据库存储已完成，已关闭数据库')
