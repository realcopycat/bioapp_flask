# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html


from scrapy import signals
import time
import logging
# useful for handling different item types with a single interface
from scrapy.utils.project import get_project_settings
import random


# 定于随机请求头
class RandowSpiderMiddleware(object):
    def process_request(self, request, spider):
        # pass
        settings = get_project_settings()
        user_agent = settings["USER_AGENT_LIST"]
        # print(user_agent)
        # 随机选择请求头
        ua = random.choice(user_agent)
        request.headers['USER-AGENT'] = ua


# 定义随机IP
class RandowProxy(object):
    def process_request(self, request, spider):
        settings = get_project_settings()
        proxy_list = settings["PROXY_LIST"]
        print("代理列表： ", proxy_list)
        proxy = random.choice(proxy_list)
        print("代理： ", proxy['ip_port'])


# 设置随机延时
class RandomDelayMiddleware(object):
    def __init__(self, delay):
        self.delay = delay

    @classmethod
    def from_crawler(cls, crawler):
        delay = crawler.spider.settings.get("DOWNLOAD_DELAY", 3)  # setting里设置的时间，注释默认为1s
        if not isinstance(delay, int):
            raise ValueError("RANDOM_DELAY need a int")
        return cls(delay)

    def process_request(self, request, spider):
        delay = random.randint(0, self.delay)
        logging.debug("### random delay: %s s ###" % delay)
        time.sleep(delay)




