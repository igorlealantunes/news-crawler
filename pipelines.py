# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

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









