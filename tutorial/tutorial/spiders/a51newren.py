# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import DmozItem

class A51newrenSpider(scrapy.Spider):
    name = "51newren"
    allowed_domains = ["51newren.com"]
    start_urls = (
        'http://www.51newren.com/',
    )

    def parse(self, response):
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
