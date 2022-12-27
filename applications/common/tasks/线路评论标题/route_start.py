# coding:utf-8
# version:python3.7
# author:Ivy

from applications.common.tasks.线路评论标题.xiecheng_route_comment_title import Xiecheng_Route
from applications.common.tasks.线路评论标题.qunaer_route_comment_title import Qunaer_Route
import asyncio
import time

qunaer = Qunaer_Route()
xiecheng = Xiecheng_Route()

class Route:
    def run(self):
        print("开始爬取各个网站的评论标题!")
        time_start=time.time()

        asyncio.run(xiecheng.getRoute())
        print("携程爬取结束")
        asyncio.run(qunaer.getRoute())
        print("去哪儿爬取结束")

        time_end=time.time()
        print(' time cost ',time_end-time_start,'s')






