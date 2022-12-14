import scrapy
import json
import datetime
import uuid
import time
from urllib import parse
from wangModel.items import TongchenTrainItem

class GwSpider(scrapy.Spider):
    name = 'gw'
    allowed_domains = ['qunar.com']
    start_urls = ['http://qunar.com/']
    today = str(datetime.date.today())
    def parse(self, response):
        with open("../files/city_cap.txt", encoding="utf-8") as f:
            for cityInfo in f:
                city_name = cityInfo.split(",")[1]
                kw = parse.quote(city_name.strip())
                currentTime = str(round(time.time() * 1000))
                time.sleep(2)
                url="https://train.qunar.com/dict/open/s2s.do?callback=jQuery172018610690190401646_1669725079415&dptStation="+kw+"&arrStation=%E6%A1%82%E6%9E%97&date="+str(datetime.date.today())+"&type=normal&user=neibu&source=site&start=1&num=500&sort=3&_="+currentTime
                yield scrapy.Request(
                    url=url,
                    callback=self.parseItem
                )

    def parseItem(self, response):
        item=TongchenTrainItem()
        data = response.text
        index = data.index("{")  # 获取第一个大括号所在的索引位置
        result = json.loads(response.text[index:-2])
        if result['ret']:
            info = result['data']
            print(info)
            item['site'] = "去哪儿旅行"  # 爬取站点
            item['place_from'] = info['dptStation']  # 出发城市
            item['place_to'] = info['arrStation']  # 目的城市
            item['date'] = str(self.today)  # 出发日期
            item['id'] = str(uuid.uuid1().hex)

            item['total_count'] = str(len(info['s2sBeanList']))  # 车次数量
            train_list=info['s2sBeanList']
            if len(info['s2sBeanList'])>0:
                for train in train_list:  # 循环车次
                    item['from_station'] = train['dptStationName']  # 开始车站
                    item['to_station'] = train['arrStationName']  # 到达车站
                    item['from_time'] = train['dptTime']  # 启程时间
                    item['to_time'] = train['arrTime']  # 到站时间
                    item['status'] = train['note']  # 状态
                    ticketState = train['seats']
                    for seatType, content in ticketState.items():  # 循环一个车次中的座位情况
                        print(seatType,content)
                        item['seat_name'] = content['seatName']  # 座位等级
                        item['seat_price'] = str(content['price'])  # 座位价格
                        item['seats_left'] = str(content['count'])  # 座位剩余数目
                        item['type'] = "火车"
                        print(item)
                        yield item