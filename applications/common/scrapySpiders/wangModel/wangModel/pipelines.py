# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import datetime
import uuid

from itemadapter import ItemAdapter
import csv
from scrapy.exceptions import DropItem
import happybase
import json
from wangModel.items import WangmodelItem
from wangModel.items import TuniuhotelItem
from wangModel.items import WeiboItem
from wangModel.items import TongchenTrainItem
from wangModel.utils.mysqlConn import insert,update

from wangModel.utils.HbaseConn import HbaseUtil


class DuplicatesPipeline(object):
    """
    去重
    """
    def __init__(self):
        self.book_set = set()

    def process_item(self, item, spider):
        name = item['id']
        if name in self.book_set:
            raise DropItem("Duplicate book found:%s" % item)

        self.book_set.add(name)
        return item


class WangmodelPipeline(object):
    def process_item(self, item, spider):
        f = open('test.csv', 'a+', encoding='utf-8')
        csv_writer = csv.writer(f)
        csv_writer.writerow([item['name'], item['begin_price'],item['satisfy_present'],item['img'],item['address'],item['time_arrange']])
        f.close()
        return item

class tuniuHBasePipeline(object):
    def __init__(self):
        # host = '192.168.174.129'
        host = '202.193.53.106'
        table_name1 = 'tuniu_scenic'
        table_name2 = 'scenic_hotel'
        hbase=HbaseUtil(host)
        self.hbase=hbase
        self.tablename1=table_name1
        self.tablename2=table_name2

    def process_item(self, item, spider):
        """
        存储途牛景点数据
        :param item:
        :param spider:
        :return:
        """
        if isinstance(item,WangmodelItem):
            host = '202.193.53.106'
            hbase = HbaseUtil(host)
            sql="INSERT INTO scenic_comment(scenicId,scenicName,satisfy_present,num,good,middle,bad,crawlTime,siteFrom) select %s,%s,%s,%s,%s,%s,%s,%s,%s from dual where not exists (select scenicName,crawlTime,siteFrom from scenic_comment where scenicName=%s and crawlTime=%s and siteFrom='途牛');"
            insert(sql,(item['id'],item['name'],item['satisfy_present'],item['remarkAmount'],item['compGrade3Amount'],item['compGrade2Amount'],item['compGrade1Amount'],datetime.date.today(),"途牛",item['name'],datetime.date.today()))
            id = item['id']
            commentlist=[]
            # print(item)
            commentlist=item['commentlist']
            obj={}
            if len(commentlist)>0:
               for data in commentlist:
                   userId=str(data['userId'])
                   userName=str(data['userName'])
                   content=str(data['content'])
                   if data['subCompGrade'] is not None:
                       others={}
                       for k,v in data['subCompGrade'].items():
                           others[k]=str(v)
                   remarkSatisfaction=str(data['remarkSatisfaction'])
                   compGrade=str(data['compGrade'])
                   key=uuid.uuid1().hex
                   print(others)
                   wibsite='途牛'
                   putInfo={
                       "info:userid": userId,
                       "info:username": userName,
                       "info:scenicid": str(item['id']),
                       "info:scenicname": item['name'],
                       "info:content": content,
                       "info:others": str(others),
                       "info:satisfaction": remarkSatisfaction,
                       "info:compgrade": compGrade,
                       "info:datafrom": "途牛",
                       "info:postDate": data['remarkTime']

                   }
                   print(putInfo)
                   try:
                        self.hbase.batchTable("scenics_comment",str(key),putInfo)
                   except:
                       self.hbase.closeCon()
                       hbase = HbaseUtil('202.193.53.106')
                       hbase.batchTable("scenics_comment",str(key),putInfo)


            """
            存储途牛酒店数据
            """
        elif isinstance(item,TuniuhotelItem):
            for child in item['hcomments']:
                print("存入Hbase",child)
                userId=child['reviewerId']
                userName=child['reviewerName']
                content=child['content']
                score=str(child['score'])
                remarkTime=child['remarkTime']

                try:
                    self.hbase.batchTable("hotel_comments", str(uuid.uuid1().hex),
                                          {
                                              'info:hid': str(item['id']),
                                              'info:hname': item['hname'],
                                              'info:userid': userId,
                                              'info:username': userName,
                                              'info:content': content,
                                              'info:score': score,
                                              'info:postDate': remarkTime,
                                          })
                except:
                    self.hbase.closeCon()
                    hbase = HbaseUtil('202.193.53.106')
                    hbase.batchTable("scenics_comment", str(key), putInfo)
                    hbase.batchTable("hotel_comments",str(uuid.uuid1().hex),
                                {
                                    'info:hid':str(item['id']),
                                    'info:hname':item['hname'],
                                    'info:userid':userId,
                                    'info:username':userName,
                                    'info:content':content,
                                    'info:score':score,
                                    'info:postDate':remarkTime,
                                })
            """
            存储微博数据:桂林官方旅游微博每一条文章
            """
        elif isinstance(item, WeiboItem):
            print("存储该页的微博文章",item['artilelist'])
            for artile_content in item['artilelist']:
                self.hbase.putTable("weibo",artile_content['artile_id'],{
                    'info:userid':str(item['userid']),
                    'info:screen_name':item['screen_name'],
                    'info:fins':item['fins'],
                    'info:total_artiles':str(item['total_artiles']),
                    'info:artile_id':artile_content['artile_id'],
                    'info:attitudes_count':artile_content['attitudes_count'],
                    'info:comments_count':artile_content['comments_count'],
                    'info:reposts_count':artile_content['reposts_count'],
                    'info:postDate':artile_content['postDate'],
                    'info:text':artile_content['text']
                })
            """
            存储同城旅游
            """

        elif isinstance(item, TongchenTrainItem):
            print("获取对象",item)
            host = '202.193.53.106'
            hbase = HbaseUtil(host)
            try:
                hbase.batchTable("leftticket", item['id'], {
                    'info:place_from': item['place_from'],  #出发城市
                    'info:place_to': item['place_to'],  #抵达城市:桂林
                    'info:date': item['date'],  #时间
                    'info:total_count': item['total_count'], #一个城市到桂林的车次数目
                    'info:from_station': item['from_station'], #出发车站名
                    'info:to_station': item['to_station'], #抵达车站名
                    'info:type': item['type'], #乘坐类型：火车/客车
                    'info:from_time': item['from_time'],#出发时间
                    'info:to_time': item['to_time'], #到达时间
                    'info:seat_name': item['seat_name'], #座位名，火车有特等坐，客车没有就不用插
                    'info:seat_price': item['seat_price'], #座位价格
                    'info:seats_left': item['seats_left'], #剩余票数
                    'info:status': item['status']  #座位状态
                })
            except:
                hbase.closeCon()
                hbase=HbaseUtil(host)
                hbase.batchTable("leftticket", item['id'], {
                    'info:place_from': item['place_from'],  # 出发城市
                    'info:place_to': item['place_to'],  # 抵达城市:桂林
                    'info:date': item['date'],  # 时间
                    'info:total_count': item['total_count'],  # 一个城市到桂林的车次数目
                    'info:from_station': item['from_station'],  # 出发车站名
                    'info:to_station': item['to_station'],  # 抵达车站名
                    'info:type': item['type'],  # 乘坐类型：火车/客车
                    'info:from_time': item['from_time'],  # 出发时间
                    'info:to_time': item['to_time'],  # 到达时间
                    'info:seat_name': item['seat_name'],  # 座位名，火车有特等坐，客车没有就不用插
                    'info:seat_price': item['seat_price'],  # 座位价格
                    'info:seats_left': item['seats_left'],  # 剩余票数
                    'info:status': item['status']  # 座位状态
                })
        return item

