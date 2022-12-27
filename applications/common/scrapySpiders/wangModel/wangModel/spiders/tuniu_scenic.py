# -*- coding:utf-8 -*-
import json
import time

import requests
import scrapy
from wangModel.items import WangmodelItem
import re
from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.common.action_chains import ActionChains
from math import ceil
from wangModel.utils.mysqlConn import query
import datetime
import re

# 2.继承RedisSprider
class ItcastSpider(scrapy.Spider):
    name = 'tuniu_scenic'
    # redis_key = 'tuniu:start_urls'  #监听此key
    allowed_domains = ['tuniu.com']

    start_urls = ['https://www.tuniu.com/menpiao/787427#/index']
    # start_urls = ["https://s.tuniu.com/search_complex/ticket-nn-0-%E6%A1%82%E6%9E%97/"]
    # start_urls = ["https://www.tuniu.com/resp-detail/api/menpiao/getMenpiaoComment?currentPage=3&specId=1167&stamp=078776045436755181667991933212"]
    flag=1

    def start_requests(self):
       url_list= query("select id,name,tn_url from scenics where tn_url !='' ",None)
       # print(self.start_urls)
       # yield scrapy.Request(
       #     url=url_list[0]['url'],
       #     callback=self.parse,
       #     meta={"scenic": url_list[0]}
       # )
       for redatas in url_list:
           time.sleep(2)
           yield scrapy.Request(
               url=redatas['url'],
               dont_filter=False,
               callback=self.parse,
               meta={"scenic":redatas}
           )
    """
    爬取列表页面
    """
    def parse(self, response):  # 处理详情页，处理json数据
        time.sleep(3)
    #     print("---------------进入详情页面爬取-----------------")
        item = WangmodelItem()
        data=response.json()
        scenic=response.meta.get('scenic')
        item['id']=scenic['id']
        item['name']=scenic['name']
        item['satisfy_present']=data['data']['summary']['satisfaction']
        item['remarkAmount']=data['data']['summary']['remarkAmount']
        item['compGrade3Amount']=data['data']['summary']['compGrade3Amount']
        item['compGrade2Amount']=data['data']['summary']['compGrade2Amount']
        item['compGrade1Amount']=data['data']['summary']['compGrade1Amount']
        commentlist=data['data']['remarkList']
        item['commentlist'] = []
        # print(item)
        # yield item

        """
        评论详情
        """
        if commentlist is not None:
            item['commentlist']=commentlist
            comment_page=ceil(item['remarkAmount']/10)  #评论页数
            if(comment_page)>1:
                flag = 1
                while flag <= comment_page:
                    currentPage=flag+1
                    flag+=1
                    productId=re.search("specId=.*&",scenic['url']).group().replace("specId=","").replace("&","")
                    detail_page_url = f"https://www.tuniu.com/resp-detail/api/menpiao/getMenpiaoComment?currentPage={currentPage}&specId={productId}&stamp=078776045436755181667991933212"
                    yield scrapy.Request(
                        url=detail_page_url,
                        callback=self.parse_detail_nextPage,
                        meta={"item": item, "url": detail_page_url,"currentPage":currentPage,"comment_page":comment_page},
                        dont_filter=True
                    )


    def parse_detail_nextPage(self, response):  # 处理详情翻页评论页，处理json数据
        time.sleep(2)
        item = response.meta.get('item')
        currentPage=response.meta.get('currentPage')
        comment_page=response.meta.get('comment_page')
        data = response.json()
        # print("翻页评论详情",data)
        commentlist = data['data']['remarkList']
        if commentlist is not None:
            item['commentlist'] =item['commentlist']+commentlist
            if currentPage==comment_page:
                yield item