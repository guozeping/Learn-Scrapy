# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymongo
from twisted.enterprise import adbapi


class FtxscrapyPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):  # 函数名固定，会被scrapy调用，直接可用settings的值
        """
        数据库建立连接
        :param settings: 配置参数
        :return: 实例化参数
        """
        adbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            cursorclass=pymysql.cursors.DictCursor  # 指定cursor类型
        )

        # 连接数据池ConnectionPool，使用pymysql或者Mysqldb连接
        dbpool = adbapi.ConnectionPool('pymysql', **adbparams)
        # 返回实例化参数
        return cls(dbpool)

    def process_item(self, item, spider):
        """
        使用twisted将MySQL插入变成异步执行。通过连接池执行具体的sql操作，返回一个对象
        """
        query = self.dbpool.runInteraction(self.do_insert, item)  # 指定操作方法和操作数据
        # 添加异常处理
        query.addCallback(self.handle_error)  # 处理异常

    def do_insert(self, cursor, item):
        # 对数据库进行插入操作，并不需要commit，twisted会自动commit
        insert_sql = """
        insert into
        """
        self.cursor.execute(insert_sql, (item['Name'], item['Address'], item['Grade'], item['Score'],
                                         item['Price']))

    def handle_error(self, failure):
        if failure:
            # 打印错误信息
            print(failure)

class ToMongoDBPipeline(object):
    conn = None

    def open_spider(self, spider):
        print("建立数据库连接...")
        self.conn = pymongo.MongoClient(host='localhost', port=27017)

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        pass

class ToMySQLPipeline(object):

    def __init__(self):
        pass
    def conn_mysql(self):
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='test', charset='utf8')

        cursor = db.cursor()
        sql = """CREATE TABLE BOOK(
                  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '自增 id',
                  book_name VARCHAR(1024) NOT NULL COMMENT '小说名',
                  author VARCHAR(1024) NOT NULL COMMENT '小说作者',
                  book_type VARCHAR(1024) NULL NULL COMMENT '小说类型',
                  book_state VARCHAR(1024) DEFAULT NULL COMMENT '小说状态',
                  book_update VARCHAR(1024) DEFAULT NULL COMMENT '小说更新',
                  book_time VARCHAR(1024) DEFAULT NULL COMMENT '更新时间',
                  new_href VARCHAR(1024) DEFAULT NULL COMMENT '最新一章',
                  book_intro VARCHAR(1024) DEFAULT NULL COMMENT '小说简介',
                  createtime DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '添加时间'
                  )"""

        cursor.execute(sql)

        db.close()

if __name__ == '__main__':
    ToMySQLPipeline().conn_mysql()