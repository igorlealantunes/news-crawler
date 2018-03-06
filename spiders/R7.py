# -*- coding: utf-8 -*-
import scrapy
from noticias.items import R7Item
import json
import sys
from scrapy.http.request import Request
import re

class R7Spider(scrapy.Spider):
    
    name = 'r7'
    
    start_urls = ['https://noticias.r7.com/brasil/noticias?mobile_cookie=false&page=1']

    pageNum = 1

    def parse(self, response):
        
        for h3 in response.css('h3.listing-title'):
            link = h3.css('a::attr(href)').extract_first()

            yield response.follow(link, self.parse_article)

        self.pageNum += 1
        next_page = "https://noticias.r7.com/brasil/noticias?mobile_cookie=false&page="+ str(self.pageNum)

        yield Request(next_page, self.parse)

    def parse_article(self, response):

        link = response.url
        title = response.css('header.heading-article h1.title ::text').extract_first()
        author = response.css('li.list-item-agency h6 ::text').extract_first()
        text = re.sub(' +',' ', ''.join(response.css('article.content p ::text').extract())).replace('\n', '')

        created = response.css('li.list-item time ::text').extract_first()
        
        notice = R7Item(title=title, author=author, text=text,
                              link=link, summary='', created=created)
        yield notice









   