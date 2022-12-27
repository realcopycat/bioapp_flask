#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：爬虫 -> 运行爬虫文件
@IDE    ：PyCharm
@Author ：sandmswift
@Date   ：2022-12-11 14:20
@Desc
=================================================='''
from scrapy.cmdline import execute
from wangModel.common_spiders.baidusearch import BaiduSpider
from wangModel.common_spiders.baiduacc import baiduacc
from wangModel.common_spiders.baiduwords import BaiDuWords
from wangModel.common_spiders.weibosign import WeiboSignSpider
from wangModel.common_spiders.tuniu_route import temp

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os
import sys

settings = get_project_settings()
crawler = CrawlerProcess(settings)

#scrapy爬虫
crawler.crawl('tongchen')
crawler.crawl('tuniu_scenic')
crawler.crawl('tuniu_hotel')
crawler.crawl('weibo')

crawler.start()
crawler.start()
crawler.start()
crawler.start()


# 爬取普通爬虫
""" 1.百度指数"""
object=baiduacc()
object.parse1()

""" 2.百度搜索"""
run = BaiduSpider()
run.parse()

"""3.百度词条"""
baiduWord = BaiDuWords()
baiduWord.run()

"""4.微博签到"""
web = WeiboSignSpider()
web.run()
