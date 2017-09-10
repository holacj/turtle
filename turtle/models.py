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

import uuid
import datetime

from turtle import db


class NewsSpiderItem(db.Document):
    """ 新闻爬虫文档"""
    uuid = db.StringField(unique=True, default=str(uuid.uuid4()))
    url = db.StringField(required=True)
    title = db.StringField(required=True)
    content = db.StringField()
    pic_link = db.StringField()
    create_time = db.DateTime(default=datetime.datetime.now)
    flag = db.IntField(default=1)
    remark = db.IntField(default=1)

    meta = {
        'collection': 'baidu_news'
    }