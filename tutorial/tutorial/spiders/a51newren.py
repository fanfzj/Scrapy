# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import DmozItem


def change_word(s):
    sum = 0
    for i in s[0]:
        sum += 1
    ss2 = ''

    for i in range(0, sum):
        if (s[0][i] == u'\u2014'):
            continue
        ss2 += s[0][i]

    s = ss2
    print s
    return s

class A51newrenSpider(scrapy.Spider):
    name = "51newren"
    allowed_domains = ["51newren.com"]
    start_urls = (
        'http://www.51newren.com/Login',
    )
    def parse(self, response):
        sel = scrapy.Selector(response)
        item = DmozItem()
        sel=scrapy.Selector(response)

        href=str(response.url)
        name=sel.xpath("//a/text()").extract()

        item['body']=href.encode('utf-8')
        item['title']=[n.encode('utf-8') for n in name]
        yield  item

        for url in sel.xpath("//a/@href").extract():
            if(str(url).encode("utf-8")[0]=='/'):
                site = "http://www.51newren.com/" + url
                yield scrapy.Request(site, callback=self.parse)