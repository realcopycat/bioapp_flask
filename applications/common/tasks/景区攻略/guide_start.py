# coding:utf-8
# version:python3.7
# author:Ivy

from applications.common.tasks.景区攻略.mafengwo_scenic import Mafengwo_Scenic
from applications.common.tasks.景区攻略.qunaer_scenic import Qunaer_Scenic
from applications.common.tasks.景区攻略.xiecheng_scenic import Xiecheng_Scenic
import asyncio
import time

mafengwo = Mafengwo_Scenic()
qunaer = Qunaer_Scenic()
xiecheng = Xiecheng_Scenic()

class Guide:
    def run(self):
        print("开始爬取各个网站的评论标题!")
        time_start=time.time()

        asyncio.run(xiecheng.getScenic())
        print("携程爬取结束")
        # asyncio.run(qunaer.getScenic())
        # print("去哪儿爬取结束")
        asyncio.run(mafengwo.getScenic())
        print("马蜂窝爬取结束")

        time_end=time.time()
        print(' time cost ',time_end-time_start,'s')






