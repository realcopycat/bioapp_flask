#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：爬虫 -> tongtencities
@IDE    ：PyCharm
@Author ：sandmswift
@Date   ：2022-11-17 11:25
@Desc   此爬虫用于爬取同城旅行的城市id信息
=================================================='''
import  requests
import json
url='https://bus.ly.com/busresapi/destination/getDesByLetter'

data={
  'letter': 'ALL',
  'depCName': '深圳',
  'depCId': 1090
}
params={
    "plateId":3
}
response=requests.post(url,json=data,params=params)
result=response.json()
city_list=result['body']
with open("../files/city.txt", "a+", encoding='utf-8') as f:
    for item in city_list:
        id=item['id']
        cityName=item['name']
        f.write(str(id))
        f.write(",")
        f.write(cityName)
        f.write("\n")
f.close()