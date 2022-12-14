#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：爬虫 -> citydeal
@IDE    ：PyCharm
@Author ：sandmswift
@Date   ：2022-11-30 20:08
@Desc
=================================================='''
import re
with open('../files/city.txt',encoding="utf-8") as f:
    for cityInfo in f:
        city_id = cityInfo.split(",")[0]
        city_name = cityInfo.split(",")[1]
        kw = city_name.strip()
        if len(re.findall("([.*镇]|[.*县]|[.*村]|[.*区]|[.*乡])",kw))==0:
            print(kw)
            with open("../files/city_cap.txt","a+",encoding='utf-8') as city:
                city.write(city_id+","+kw+"\n")

# data="灌阳县"
# data1="灌阳镇"
# data2="灌阳村"
#
# print(len(re.findall("([.*镇]|[.*县]|[.*村])",data))>0)
# print(re.findall("([.*镇]|[.*县]|[.*村])",data1))
# print(re.findall("([.*镇]|[.*县]|[.*村])",data2))
