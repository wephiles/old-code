# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class QiutuProjectPipeline:
    # 专门用来处理item类型对象
    # 该方法可以接受爬虫文件传过来的item对象
    # 该方法每接受一次item，则调用这个方法一次
    fp = None
    # 重写父类的方法 该方法只在开始爬虫的时候调用一次

    def open_spider(self, spider):
        print('Crawl begin ... ')
        self.fp = open('qiutu_pipe.csv', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        author = item['name']
        talk = item['content']
        self.fp.write(author + ': ' + talk + '\n')
        return item
    # 该方法只会在爬虫结束时被调用一次

    def close_spider(self, spider):
        print('Crawl end! ')
        self.fp.close()
# 管道文件中，一个管道类对应将一个数据存储到一个平台或者载体中


class MySQLPipeline:
    connection = None
    cursor = None  # 游标对象

    def open_spider(self, spider):
        self.connection = pymysql.Connect(host='127.0.0.1',port=3306, user='root', password='bws20000807', db='qiutu_baike', charset='utf8')

    def process_item(self, item, spider):
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute('insert into qiutu_baike values("%s", "%s")%(item["name"],item["content"])')
            self.connection.commit()
        except Exception as e:
            print(e)
            self.connection.rollback()
        return item  # 就会传递给下一个将要被执行的管道类

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()

# 爬虫文件提交的item最终会提交给哪一个管道类？？？一定先给优先级高的管道类
