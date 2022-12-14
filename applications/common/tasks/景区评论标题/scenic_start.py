# coding:utf-8
# version:python3.7
# author:Ivy

from applications.common.tasks.景区评论标题.mafengwo_scenic_comment_title import Mafengwo_Scenic
from applications.common.tasks.景区评论标题.qunaer_scenic_comment_title import Qunaer_Scenic
from applications.common.tasks.景区评论标题.tongcheng_scenic_comment_title import Tongcheng_Scenic
from applications.common.tasks.景区评论标题.xiecheng_scenic_comment_title import Xiecheng_Scenic
import asyncio
import time

mafengwo = Mafengwo_Scenic()
qunaer = Qunaer_Scenic()
tongcheng = Tongcheng_Scenic()
xiecheng = Xiecheng_Scenic()

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






