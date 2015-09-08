# -*- coding: utf-8 -*-
import pymssql
import scrapy
import json
from scrapy.selector import Selector
from tutorial.items import DmozItem
from scrapy.http import Request

class WeatherSpider(scrapy.Spider):
    name = "weather"
    allowed_domains = ["etouch.cn"]
    start_urls = (
        'http://wthrcdn.etouch.cn/weather_mini?city=北京',
    )

    def parse(self, response):
        item = DmozItem()
        sites =Selector(text=response.body)
        detail_url_list = sites.xpath('//p/text()').extract()
        for site in detail_url_list:
            item["json"]=json.loads(site)

        jsons=json.dumps(item["json"])
        ddata=json.loads(jsons)
        print ddata['data']['forecast'][0]

        # conn = pymssql.connect(host="121.42.136.4", user="sa", password="koala19920716!@#", database="test")
        # cursor = conn.cursor()
        # print sel
        # for site in sel['data']:
        #     print site
        # for site in sel['data']:
        #     sql = "Insert into Weather(CityName)values('" + site['city'] + "')"
        #     cursor.execute(sql)
        #     conn.commit()
        #
        # sql = "select CityName from Cities"
        # cursor.execute(sql)
        # for (CityName) in cursor.fetchall():
        #     print CityName
        #     url = "http://wthrcdn.etouch.cn/weather_mini?city=" + CityName
        #     yield Request(url, callback=self.parse)
