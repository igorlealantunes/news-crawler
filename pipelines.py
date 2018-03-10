# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import sys
#import MySQLdb
import pymysql
import pymysql.cursors
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request


class NoticiasPipeline(object):

    def open_spider(self, spider):
      self.file = open('notices.txt', 'w')

    def close_spider(self, spider):
      self.file.close()

    def process_item(self, item, spider):
      line =  json.dumps(dict(item), ensure_ascii=False)  + '\n'
      self.file.write(line)
      return item


class G1JsonPipeline(object):

    def open_spider(self, spider):
        self.file = open('g1-notices.txt', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line =  json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item


class IGPipeline(object):

    def open_spider(self, spider):
        self.file = open('ig-notices.txt', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line =  json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item

class R7Pipeline(object):

    def open_spider(self, spider):
        self.file = open('r7-notices.txt', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line =  json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item

"""
MYSQL storage:
"""
"""
class NewsObjectDBPipeline(object):
    
    def __init__(self):
        self.conn = MySQLdb.connect(host='localhost', user='root', passwd='root', db='mapa_pressao-01', port=8889, charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):    
        try:
            self.cursor.execute("INSERT INTO News (Title, Author, Body, Source, CreatedAt)  
                                    VALUES (%s, %s, %s, %s)",

                                (
                                    item['title'].encode('utf-8'), 
                                    item['author'].encode('utf-8'),
                                    item['text'].encode('utf-8'),
                                    item['source'].encode('utf-8'),
                                    item['created'].encode('utf-8') 
                                )
                        )

            self.conn.commit()


        except e:
            print("DB ERROR")
            print(e)
            print(e.args[0])
            print(e.args[1])


        return item
"""

class NewsObjectDBPipeline(object):
    
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='mapa_pressao-01',
                             charset='utf8',
                             port=8889,
                             cursorclass=pymysql.cursors.DictCursor)

    def process_item(self, item, spider):    
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO News (Title, Author, Body, Source, CreatedAt) VALUES (%s, %s, %s, %s)"
                
                cursor.execute(sql, 
                                (
                                    item['title'].encode('utf-8'), 
                                    item['author'].encode('utf-8'),
                                    item['text'].encode('utf-8'),
                                    item['source'].encode('utf-8'),
                                    item['created'].encode('utf-8') 
                                ))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()

        return item

