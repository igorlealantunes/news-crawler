# -*- coding: utf-8 -*-
import scrapy
from noticias.items import IGItem
import json
import sys
from scrapy.http.request import Request
import re

class IGSpider(scrapy.Spider):
    
    name = 'ig'
    
    start_urls = ['http://ultimosegundo.ig.com.br/_indice/noticias/select?start=0&size=20&site=ultimosegundo&secoes_eh=4ea6ff6af4cc0e9f760003c4&wt=json']

    pageNum = 0

    def parse(self, response):
        
        # Getting metadata for the news in a json format
        jsonresponse = json.loads(response.body_as_unicode())

        for new in jsonresponse['response']['docs']:

            yield response.follow(new['url'], self.parse_article)

        # creates the url for the next page 
        next_page = str(self.pageNum + 1)

        self.pageNum = self.pageNum + 1

        url = 'http://ultimosegundo.ig.com.br/_indice/noticias/select?start=' + str(self.pageNum) + '&size=20&site=ultimosegundo&secoes_eh=4ea6ff6af4cc0e9f760003c4&wt=json'

        yield Request(url, self.parse)

    def parse_article(self, response):

        link = response.url
        title = response.css('h1#noticia-titulo-h1 ::text').extract_first()
        author = response.css('span#authors-box strong ::text').extract_first()
        text = re.sub(' +',' ', ''.join(response.css('section.noticia p ::text').extract())).replace('\n', '')

        created = response.css('span#dataHTML time ::text').extract_first()
        
        notice = IGItem(title=title, author=author, text=text,
                              link=link, summary='', created=created)
        yield notice









   