# -*- coding: utf-8 -*-
import sys

import scrapy
from scrapy.http import Request
from scrapy.selector import Selector

from tutorial.items import DmozItem

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
    download_delay = 1
    allowed_domains = ["blog.csdn.net"]
    start_urls = [
        "http://blog.csdn.net/u012150179/article/details/11749017"
    ]

    def parse(self, response):
        sel = Selector(response)
        item = DmozItem()
        # ISOTIMEFORMAT = '%Y-%m-%d %X'
        # datetime=time.strftime(ISOTIMEFORMAT,time.localtime())
        # conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='blog',port=3306,charset='utf8')
        # cursor = conn.cursor()

        article_url = str(response.url)
        article_name = sel.xpath('//div[@id="article_details"]/div/h1/span/a/text()').extract()
        article_body = sel.xpath('//div[@id="article_details"]/div[@id="article_content"]').extract()
        article_label = sel.xpath('//div[@class="article_manage"]/span[@class="link_categories"]/a/text()').extract()
        if (len(article_body) != 0):
            if (len(article_label) != 0):
                item['body'] = article_body[0].encode('utf-8')
                item['article_label'] = article_label[0].encode('utf-8')
                item['article_name'] = article_name[0].encode('utf-8')
                item['article_url'] = article_url.encode('utf-8')
            else:
                print article_url + "   article_label"
            print article_url + "      " + str([n.encode('utf-8') for n in article_name])
        else:
            print article_url + "   article_body"
        urls = sel.xpath('//li[@class="next_article"]/a/@href').extract()
        for url in urls:
            url = "http://blog.csdn.net" + url
            # print type(url)
            yield Request(url, callback=self.parse)
