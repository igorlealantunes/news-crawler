# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NoticiasItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()
    summary = scrapy.Field()
    created = scrapy.Field()
    link = scrapy.Field()

class IGItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()
    summary = scrapy.Field()
    created = scrapy.Field()
    link = scrapy.Field()

class G1JsonItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()
    summary = scrapy.Field()
    created = scrapy.Field()
    link = scrapy.Field()
