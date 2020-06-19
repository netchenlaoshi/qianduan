# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockspiderItem(scrapy.Item):
    code = scrapy.Field()
    name=scrapy.Field()
    liutongshizhi=scrapy.Field()
    zongshizhi=scrapy.Field()
    liutongguben=scrapy.Field()
    zongguben=scrapy.Field()
    pass
