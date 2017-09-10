#!/usr/bin/env python
#   -*- coding: UTF-8 -*-
#
#   Copyright (C) 2017 Chenji
# 
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
# 
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
# 
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json
from scrapy import Spider

from turtle.news.baidu_news.baidu_news.items import BaiduNewsItem


class BaiduHomeNewsSpider(Spider):
    """ 百度新闻爬虫-首页"""
    name = 'spider_baidu_home_news'
    start_urls = [
        "http://news.baidu.com/widget?id=LocalNews&ajax=json"
    ]

    def parse(self, response):
        body = response.body
        body_en_json = json.loads(body)
        data = body_en_json.get("data")
        news = data.get("LocalNews")
        data = news.get("data")
        rows = data.get("rows")
        items = rows.get("first")
        for it in items:
            item = BaiduNewsItem()
            item["url"] = it.get("url")
            item["create_time"] = it.get("time")
            item["pic_url"] = it.get("imgUrl")
            item["title"] = it.get("title")
            yield item

