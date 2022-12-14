#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：pear-admin-flask -> weibosign
@IDE    ：PyCharm
@Author ：sandmswift
@Date   ：2022-12-14 18:14
@Desc
=================================================='''
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from wangModel.common_spiders.weibosign import WeiboSignSpider

settings = get_project_settings()
crawler = CrawlerProcess(settings)


class WeiBoSign:

    def run(self):
        print("开始爬取微博签到")
        web = WeiboSignSpider()
        web.run()
        print("爬取微博签到结束")
