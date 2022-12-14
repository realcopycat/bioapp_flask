# coding:utf-8
# version:python3.7
# author:Ivy

from applications.common.tasks.酒店评论标题.xiecheng_hotel_comment_title import Xiecheng_Hotel
from applications.common.tasks.酒店评论标题.qunaer_hotel_comment_title import Qunaer_Hotel
from applications.common.tasks.酒店评论标题.tongcheng_hotel_comment_title import Tongcheng_Hotel
import asyncio
import time
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
settings = get_project_settings()
crawler = CrawlerProcess(settings)

qunaer = Qunaer_Hotel()
tongcheng = Tongcheng_Hotel()
xiecheng = Xiecheng_Hotel()

class Hotel:
    def run(self):
        print("开始爬取各个网站的评论标题!")
        time_start=time.time()

        asyncio.run(xiecheng.getHotel())
        print("携程爬取结束")
        asyncio.run(tongcheng.getHotel())
        print("同程爬取结束")
        asyncio.run(qunaer.getHotel())
        print("去哪儿爬取结束")

        crawler.crawl('tuniu_hotel')
        crawler.start()
        print("途牛酒店爬取结束")

        time_end=time.time()
        print(' time cost ',time_end-time_start,'s')






