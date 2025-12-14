# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class EmbarrassmentPipeline:
    fp = None

    # 重写父类方法 该方法只在开始爬虫时调用一次
    def open_spider(self, spider):
        print('开始爬虫')
        self.fp = open('qiubai.txt', 'w', encoding='utf-8')

    # 专门用来处理item对象 可以接受爬虫文件提交过来的item对象
    def process_item(self, item, spider):
        # 每接受一个item 调用一次 肯定会被调用多次
        number = item['number']
        title = item['title']
        self.fp.write(title + ' - ' + number + '\n')
        return item

    # 只在结束爬虫打印一次
    def close_spider(self, spider):
        print('结束爬虫')
        self.fp.close()


# 管道文件中 一个管道类对应将一组数据存储到一个载体中
class MySQLPipeLine(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            password='WarmDou_TS20866',
            db='runoob',
            charset='utf8'
        )

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('INSERT INTO sites (name, url) VALUES("%s", "%s")' % (item["number"], item["title"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()


