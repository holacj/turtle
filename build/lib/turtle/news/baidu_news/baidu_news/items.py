# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduNewsItem(scrapy.Item):
    """ 百度新闻-首页item"""
    url = scrapy.Field()
    pic_url = scrapy.Field()
    create_time = scrapy.Field()
    title = scrapy.Field()

