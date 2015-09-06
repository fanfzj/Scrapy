# -*- coding: utf-8 -*-
import scrapy
import sys
from tutorial.items import DmozItem
from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector

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
    allowed_domains = ["http://so.csdn.net/so/search/s.do?q=python&q=python"]
    start_urls = (
        'http://php.itcast.cn/',
    )


    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="huodong11"]/li')
        for site in sites:
            temp=site.xpath('a/span/text()').extract()
            if(len(temp)!=0):
                change_word(temp)
                print "-----------------------------------------------"
