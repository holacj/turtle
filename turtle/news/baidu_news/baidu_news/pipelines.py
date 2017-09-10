# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from turtle.models import NewsSpiderItem


class BaiduNewsPipeline(object):
    def process_item(self, item, spider):
        NewsSpiderItem(
            url=item["url"],
            pic_url=item["pic_url"],
            create_time=item["create_time"],
            title=item["title"]
        ).save()
