#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：爬虫 -> weather_deal
@IDE    ：PyCharm
@Author ：sandmswift
@Date   ：2022-12-13 12:13
@Desc
=================================================='''
from mysqlConn import getRows,update

select_westher="select id,max_tem,min_tem,"
