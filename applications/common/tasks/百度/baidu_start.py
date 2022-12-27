#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：pear-admin-flask -> baidu_start
@IDE    ：PyCharm
@Author ：sandmswift
@Date   ：2022-12-14 18:20
@Desc
=================================================='''
from wangModel.common_spiders.baiduacc import baiduacc
from wangModel.common_spiders.baidusearch import BaiduSpider
from wangModel.common_spiders.baiduwords import BaiDuWords


class BaiduCrawl:
    def run(self):
        # 爬取普通爬虫
        """ 1.百度指数"""
        print("开始爬取百度指数")
        object = baiduacc()
        object.parse1()
        print("百度指数爬取完毕")

        """ 2.百度搜索"""
        print("开始爬取百度搜索")
        run = BaiduSpider()
        run.parse()
        print("百度搜索爬取完毕")

        """3.百度词条"""
        print("开始爬取百度词条")
        baiduWord = BaiDuWords()
        baiduWord.run()
        print("百度词条爬取完毕")