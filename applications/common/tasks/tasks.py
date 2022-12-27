from applications.common.tasks.微博签到.weibosign import WeiBoSign
from applications.common.tasks.景区评论标题.scenic_start import Scenic
from applications.common.tasks.百度.baidu_start import BaiduCrawl
from applications.common.tasks.线路评论标题.route_start import Route
from applications.common.tasks.酒店评论标题.hotel_title_start import Hotel
from applications.common.tasks.景区攻略.guide_start import Guide
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

settings = get_project_settings()
crawler = CrawlerProcess(settings)

task_list = ['景区评论标题', '线路评论标题', '景区攻略', '酒店评论标题']


def 景区评论标题(id, name):
    scenic_start = Scenic()
    scenic_start.run()


def 线路评论标题(id, name):
    scenic_start = Route()
    scenic_start.run()


def 景区攻略(id, name):
    scenic_start = Guide()
    scenic_start.run()


def 酒店评论标题(id, name):
    scenic_start = Hotel()
    scenic_start.run()


def 交通拥堵爬取():
    crawler.crawl('tongchen')  # 只爬取同城火车票和汽车票
    crawler.start()


def 微博签到爬取():
    webosign = WeiBoSign()
    webosign.run()


def 百度相关指数爬取():
    baidu_start = BaiduCrawl()
    baidu_start.run()
