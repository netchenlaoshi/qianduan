# -*- coding: utf-8 -*-
import scrapy

from stockSpider.items import StockspiderItem
# import  sys
# print(sys.path)


class StockstarSpider(scrapy.Spider):
    name = 'stockStar'
    allowed_domains = ['quote.stockstar.com']
    start_urls = ['https://quote.stockstar.com/stock/sha.shtml']

    def parse(self, response):
        item=StockspiderItem()
        item['code']=response.xpath('//*[@id="datalist"]/tr[1]/td[1]/a/text()').extract()[0]
        item['name']=response.xpath('//*[@id="datalist"]/tr[1]/td[2]/a/text()').extract()[0]
        item['liutongshizhi']=response.xpath('//*[@id="datalist"]/tr[1]/td[3]/text()').extract()[0]


        print("code",item['code'])
        print("name",item['name'])
        print("liutongshizhi", item['liutongshizhi'])