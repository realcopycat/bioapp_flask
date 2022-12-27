import time

import scrapy
from wangModel.items import WeiboItem
from math import ceil
import re
import uuid

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.com']
    start_urls = ['http://weibo.com/']
    articles_url = "https://m.weibo.cn/api/container/getIndex?uid=1989772524&luicode=10000011&lfid=100103type=3&q=桂林旅游&t=&type=uid&value=1989772524&containerid=1076031989772524"

    total_pages=0
    current_page=1
    #https://weibo.com/ajax/profile/info?screen_name=桂林市文化广电和旅游局
    #微博列表：https://weibo.com/ajax/statuses/mymblog?uid=1989772524&page=1&feature=0
    def start_requests(self):
        yield scrapy.Request(
            url="https://m.weibo.cn/api/container/getIndex?uid=1989772524&luicode=10000011&lfid=100103type%3D3%26q%3D%E6%A1%82%E6%9E%97%E6%97%85%E6%B8%B8%26t%3D&type=uid&value=1989772524&containerid=1005051989772524",
            callback=self.parse,
        )
    #解析，获取用户的粉丝数等信息
    def parse(self, response):
        data=response.json()
        item=WeiboItem()
        item['userid']=data['data']['userInfo']['id']
        item['screen_name']=data['data']['userInfo']['screen_name']
        item['fins']=data['data']['userInfo']['followers_count_str']
        item['artilelist']=[]

        yield scrapy.Request(
            url=self.articles_url,
            callback=self.parse_articles,
            dont_filter=True,
            meta={"item":item}
        )


    # 翻页解析每一页的博客
    def parse_articles(self, response):
        item=response.meta.get('item')
        item['id'] = str(uuid.uuid1().hex)
        artilePage=response.json()
        if 'cardlistInfo' in artilePage['data']:
            nextPage_id=artilePage['data']['cardlistInfo']['since_id'] #下一页的搜索参数
            item['total_artiles']=artilePage['data']['cardlistInfo']['total']
            self.total_pages=ceil(artilePage['data']['cardlistInfo']['total']/12)
            print(f"一共有{self.total_pages}页")
            content_list=artilePage['data']['cards']  #博客列表
            card=[]
            item['artilelist']=[]
            for i in range(len(content_list)):
                card_type=content_list[i]['card_type']
                if card_type==9:
                    print(content_list[i]['mblog']['id'])
                    artile_id=content_list[i]['mblog']['id'] #博客id
                    reposts_count=content_list[i]['mblog']['reposts_count']  #转发数
                    comments_count=content_list[i]['mblog']['comments_count'] #评论数
                    attitudes_count=content_list[i]['mblog']['attitudes_count'] #点赞数
                    content_text = re.sub("[A-Za-z0-9\!\%\[\]\,\。\<\-\=\"\:\/\.\?\&\_\>\'\;\ ]", "",
                                     content_list[i]['mblog']['text'])
                    postDate = content_list[i]['mblog']['created_at']
                    card.append({
                        "artile_id":str(artile_id),
                        "reposts_count":str(reposts_count),
                        "comments_count":str(comments_count),
                        "attitudes_count":str(attitudes_count),
                        "text":str(content_text),
                        'postDate':postDate
                    })
        # item['artilelist']= item['artilelist']+card
        item['artilelist']= card
        print(f"爬取第{self.current_page}页")
        while self.current_page <= self.total_pages:
            time.sleep(2)
            yield scrapy.Request(
                url=self.articles_url + "&since_id=" + str(nextPage_id),
                callback=self.parse_articles,
                dont_filter=True,
                meta={"item": item}
            )
            print(f"-----------------第{self.current_page}页爬取完毕----------------")
            self.current_page = self.current_page + 1
            yield item

