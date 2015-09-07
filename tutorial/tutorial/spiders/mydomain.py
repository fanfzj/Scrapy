# -*- coding: utf-8 -*-
import scrapy
import sys
from tutorial.items import DmozItem
from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector

reload(sys)
sys.setdefaultencoding('utf-8')

def change_word(s):
        sum=0
        for i in s[0]:
            sum+=1
        ss2=''

        for i in range(0,sum):
            if(s[0][i]==u'\u2014'):
                continue
            ss2+=s[0][i]

        s=ss2
        print s

class MydomainSpider(scrapy.Spider):
    name = "mydomain"
    start_urls = ['http://www.baidu.com/s?wd=python&ie=utf-8']

    def parse(self, response):
        sel = Selector(response)
        items=[]
        sites=sel.xpath('//div[@id="content_left"]/div')
        item=DmozItem()
        article_url = sites.xpath('//h3/a/@href').extract()
        article_name = sites.xpath('//h3/a/text()').extract()
        article_body= sites.xpath('//div[@class="c-abstract"]').extract()

        item['title']= [n.encode('utf-8') for n in article_name]
        item['link']= [n.encode('utf-8') for n in article_url]
        item['body']=[n.encode('utf-8') for n in article_body]
        items.append(item)
        yield item
        #yield items
        # for a_item in article_name:
        #     item=DmozItem()
        #     item['title']= a_item
        #     yield item
        #     items.append(item)
        # for a_item in article_url:
        #     item=DmozItem()
        #     item['link']= a_item
        #     yield item
        #     items.append(item)
        # for a_item in article_body:
        #     item=DmozItem()
        #     item['body']=a_item
        #     items.append(item)
        #     yield item
        # yield items

        for url in sel.xpath('//div[@id="page"]').extract():
            url="https://www.baidu.com"+url
            yield Request(url,callback=self)
