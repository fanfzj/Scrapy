import scrapy

from tutorial.items import DmozItem
from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector

import sys

reload(sys)
sys.setdefaultencoding('gbk')

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
        return s

class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    download_delay = 1
    allowed_domains = ["blog.csdn.net"]
    start_urls = [
        "http://blog.csdn.net/u012150179/article/details/11749017"
    ]

    def parse(self, response):
        sel = Selector(response)
        item = DmozItem()

        article_url = str(response.url)
        article_name = sel.xpath('//div[@id="article_details"]/div/h1/span/a/text()').extract()
        article_body= sel.xpath('//div[@id="article_details"]/div[@id="article_content"]/p').extract()

        item['article_name'] = [n.encode('utf-8') for n in article_name]
        item['article_url'] = article_url.encode('utf-8')
        item['body']= [n.encode('utf-8') for n in article_body]
        yield item

        urls = sel.xpath('//li[@class="next_article"]/a/@href').extract()
        for url in urls:
            url = "http://blog.csdn.net" + url
            yield Request(url, callback=self.parse)