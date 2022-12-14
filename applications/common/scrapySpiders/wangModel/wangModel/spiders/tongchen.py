import time
import uuid

import scrapy
from urllib import parse
from wangModel.items import TongchenTrainItem
import json
import datetime
from scrapy.http import JsonRequest

from wangModel.utils.HbaseConn import HbaseUtil
"""
同城旅行爬取今日火车票
"""
class TongchenSpider(scrapy.Spider):
    name = 'tongchen'
    allowed_domains = ['ly.com']
    start_urls = ['http://ly.com/']
    today = str(datetime.date.today())



    def start_requests(self):
        with open("../files/city_cap.txt",encoding="utf-8") as f:
            car_url = "https://bus.ly.com/busresapi/schedule/getScheduleList?plateId=3"
            for cityInfo in f:
                item = TongchenTrainItem()
                city_id=cityInfo.split(",")[0]
                city_name=cityInfo.split(",")[1]
                kw = parse.quote(city_name.strip())
                currentTime=str(round(time.time()*1000))
                print("-------------正在爬取的城市是 %s-----------------"%kw)
                train_url = "https://www.ly.com/uniontrain/trainapi/TrainPCCommon/SearchTrainRemainderTickets?callback=jQuery18305629279457315504_1668857363483&para={%22To%22:%22%E6%A1%82%E6%9E%97%22,%22From%22:%22" + kw + "%22,%22TrainDate%22:%22" + self.today + "%22,%22PassType%22:%22%22,%22TrainClass%22:%22%22,%22FromTimeSlot%22:%22%22,%22ToTimeSlot%22:%22%22,%22FromStation%22:%22%22,%22ToStation%22:%22%22,%22SortBy%22:%22fromTime%22,%22callback%22:%22%22,%22tag%22:%22%22,%22memberId%22:%22%22,%22constId%22:%22TzXdqT-dUJYltDmsdvGtjh4huQTPXw1489UB3g7-exI%22,%22headct%22:%220%22,%22platId%22:1,%22headver%22:%221.0.0%22,%22headtime%22:1668590089068}&_="+currentTime


                """
                  1.爬取火车票剩余数量情况
                 """
                yield scrapy.Request(
                    url=train_url,
                    callback=self.parse_item,
                    dont_filter=False,
                    meta={"item": item}
                )

                json_request={
                        "departure": city_name.strip(),
                        "destination": "桂林",
                        "departureDate": self.today,
                        "depId": city_id,  #城市id
                        "desId": 1101,
                        "page": 1,
                        "pageSize": 25,
                        "orderTime": 0,
                        "orderPrice": 0,
                        "dptTimeSpan": "",
                        "departureStation": "",
                        "arrivalStation": "",
                        "hasCategory": True
                    }
                """
                2.爬取汽车票剩余票数情况
                """
                yield JsonRequest(
                    url=car_url,
                    callback=self.parse_car,
                    data=json_request,
                    dont_filter=False,
                    meta={"item":item,"departure":city_name.strip()}
                )

    """
    解析火车票
    """
    def parse_item(self, response):
        item=response.meta.get('item')
        data=response.text

        index=data.index("{")  #获取第一个大括号所在的索引位置
        result=json.loads(response.text[index:-1])
        info=result['data']
        print("网页响应火车票数据",info)
        if info is not None:
            flag = result['data']['trains']
            if len(flag)>0:
                item['site']="同城旅行"  #爬取站点
                item['place_from']=info['from']  #出发城市
                item['place_to']=info['to']        #目的城市
                item['date']= str(self.today) #出发日期
                item['total_count']=str(info['totalCount']) #车次数量
                train_list=result['data']['trains']
                list=[]
                for train in train_list: #循环车次
                    item['from_station']=train['fromCity']  #开始车站
                    item['to_station']=train['toCity']   #到达车站
                    item['from_time']=train['fromTime']  #启程时间
                    item['to_time']=train['toTime']  #到站时间
                    ticketState= train['ticketState']

                    for seatType,content in ticketState.items(): #循环一个车次中的座位情况
                        item['id'] = str(uuid.uuid1().hex)
                        item['seat_name']=content['cn'] #座位等级
                        item['seat_price']=content['price'] #座位价格
                        item['seats_left']=content['seats'] #座位剩余数目
                        item['type']="火车"
                        item['status']=content['state'] #状态 1表示有票，表示无票
                        yield item
                        # print("火车票",item)

    "解析汽车票"
    def parse_car(self, response):
        item = response.meta.get('item')
        departure=response.meta.get('departure')
        responseData=response.json()
        status=responseData['header']['isSuccess']
        # print("汽车票网页响应数据",responseData)
        if status==True:
            print("汽车票网页响应数据", responseData)
            cars_list=responseData['body']['schedule']
            item['site'] = "同城旅行"  # 爬取站点
            item['place_from'] = departure  # 出发地
            item['place_to'] = "桂林"  # 目的地
            item['date'] = str(self.today)  # 出发日期
            item['type']="客车"
            item['total_count'] = str(len(cars_list))  # 车次数量
            for car in cars_list:
                item['id'] = str(uuid.uuid1().hex)
                item['seat_name'] = ""  # 座位等级ticketPrice
                item['seat_price'] = str(car['ticketPrice'])  # 座位价格
                item['from_station']=car['dptStation']
                item['to_station']=car['arrStation']
                item['from_time']=car['dptTime']
                item['to_time']=""
                item['seats_left']=car['ticketLeft']
                item['status']=car['bookingDesc'] #售票状态
                yield item
        # print("汽车票",item)