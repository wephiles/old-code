# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class Douban250Pipeline:
    """
    专门用于处理items类型对象的方法
    """
    fp = None

    def open_spider(self, spider):
        """
        重写父类的方法，该方法只在开始爬虫的时候调用一次
        Args:
            spider ():

        Returns:

        """
        print('开始爬虫...')
        self.fp = open("./douban.txt", 'a', encoding='utf-8')
        pass

    def process_item(self, item, spider):
        """
        这个方法可以接受爬虫文件提交过来的item对象
        每接受一个item就会被调用一次
        Args:
            item ():
            spider ():

        Returns:

        """
        title = item['title']
        quotes = item['quotes']
        self.fp.write(title + ':' + quotes + '\n')
        # 就会传递给下一个即将执行的管道类
        return item

    def close_spider(self, spider):
        """
        重写父类方法，该方法只会在爬虫结束的时候运行一次
        Args:
            spider ():

        Returns:

        """
        self.fp.close()
        print('爬虫结束！')


# 管道文件中 一个管道类对应将一组数据存储到一个平台或载体中
class MySQLPipeline(object):

    conn = None
    cursor = None

    def open_spider(self, spider):
        """
        重写父类的方法，该方法只在开始爬虫的时候调用一次
        Args:
            spider ():

        Returns:

        """
        print('开始爬虫...')
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='637847',
            db='douban',
            charset='utf8'
        )
        pass

    def process_item(self, item, spider):
        """
        这个方法可以接受爬虫文件提交过来的item对象
        每接受一个item就会被调用一次
        Args:
            item ():
            spider ():

        Returns:

        """
        self.cursor = self.conn.cursor()
        title = item['title']
        quotes = item['quotes']
        sql = 'insert into movie (title, quotes) values (%s, %s);'
        try:
            self.cursor.execute(sql, [title, quotes])
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        """
        重写父类方法，该方法只会在爬虫结束的时候运行一次
        Args:
            spider ():

        Returns:

        """
        self.cursor.close()
        self.conn.close()
        print('爬虫结束！')
