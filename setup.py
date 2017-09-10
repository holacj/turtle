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

from setuptools import setup, find_packages

setup(
    name="turtle",                                    # 包名称
    version="1.0.0",                                  # 包版本
    classifiers=[
        "Programming Language :: Python :: 2.7",
    ],
    description="百度新闻爬虫",                         # 程序描述
    license="GPL",                                    # 程序授权信息

    author="chenji",                                  # 发布者
    packages=find_packages()                          # 需要处理的包目录(包含__init__.py的文件夹)
)