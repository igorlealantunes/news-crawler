# -*- coding: utf-8 -*-
import scrapy
from noticias.items import IGItem
import json
import sys
from scrapy.http.request import Request
import re

class IGSpider(scrapy.Spider):
    
    name = 'ig'
    
    custom_settings = {
        'ITEM_PIPELINES': {
            'noticias.pipelines.IGPipeline': 300
        }
    }


    """
        URL Brasil : http://ultimosegundo.ig.com.br/_indice/noticias/select?start=20&size=20&site=ultimosegundo&secoes_eh=4e7b7d9c7a6504a01e0000bb%204e7b7e217a6504a01e0000bd%204eb2bc4e477114d03600142f%204ea7017bf4cc0e9f760003d2%204ea701b4f4cc0e9f760003d7%204ea701f7b22976a362000619%204ea7021df4cc0e9f760003dd%204ea70273f4cc0e9f760003df%204ea70239b22976a36200061c%204ea70294b22976a36200061f%204ea702ecb22976a362000623%204ea702bef4cc0e9f760003e3%204ea7032bb22976a362000625%204ea70350b22976a362000628%204ea7037ab22976a36200062c%204ea80edf116e663972000010%2054c8e578e4d9a86c740019f6&wt=json
    """





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









   