# coding:utf-8
# version:python3.7
# author:Ivy

from applications.common.tasks.微博景区.weibo_scenic_fans import Weibo_Fans
from applications.common.tasks.微博景区.weibo_scenic_trend import Weibo_Trend
from applications.common.tasks.微博景区.weibo_scenic_wordbygeo import Weibo_Wordbygeo
from applications.common.tasks.微博景区.search_360 import Search_360
import asyncio
import time

mafengwo = Weibo_Fans()
qunaer = Weibo_Trend()
tongcheng = Weibo_Wordbygeo()
xiecheng = Search_360()

class Scenic:
    def run(self):
        print("开始爬取各个网站的评论标题!")
        time_start=time.time()

        asyncio.run(xiecheng.getScenic())
        print("携程爬取结束")
        asyncio.run(tongcheng.getScenic())
        print("同程爬取结束")
        asyncio.run(qunaer.getScenic())
        print("去哪儿爬取结束")
        asyncio.run(mafengwo.getScenic())
        print("马蜂窝爬取结束")

        time_end=time.time()
        print(' time cost ',time_end-time_start,'s')






