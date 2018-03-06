# -*- coding: utf-8 -*-
import scrapy
from noticias.items import G1JsonItem
import json
import sys

class G1Spider(scrapy.Spider):
    name = 'g1'
    #allowed_domains = ['https://falkor-cda.bastian.globo.com/feeds/8d7daa58-07fd-45c9-b1fe-aaa654957850/posts/page']
    start_urls = ['https://falkor-cda.bastian.globo.com/feeds/8d7daa58-07fd-45c9-b1fe-aaa654957850/posts/page/1']

    pageNum = 1

    def parse(self, response):
        
        # Getting metadata for the news in a json format
        jsonresponse = json.loads(response.body_as_unicode())

        for new in jsonresponse['items']:

            # Pode se fazer um filtro aqui por palavras chave
            # yield G1JsonItem(title=new['content']['title'] + str(self.pageNum), author="author", text='',
            #                 link=new['content']['url'], summary=new['content']['summary'], created=new['created'])

            yield response.follow(new['content']['url'], self.parse_article)

        # creates the url for the next page 
        next_page = str(self.pageNum + 1)

        self.pageNum = self.pageNum + 1
        yield response.follow(next_page, self.parse)

    def parse_article(self, response):

        link = response.url
        title = response.css('h1.content-head__title ::text').extract_first()
        author = response.css('p.content-publication-data__from ::text').extract_first()
        text = ''.join(response.css('p.content-text__container ::text').extract())

        created = response.css('p.content-publication-data__updated time ::text').extract_first()
        
        notice = G1JsonItem(title=title, author=author, text=text,
                              link=link, summary='', created=created)
        yield notice









   