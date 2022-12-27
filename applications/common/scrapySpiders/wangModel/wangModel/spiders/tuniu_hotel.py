import time
import scrapy
import json
from scrapy.http import JsonRequest
from wangModel.items import TuniuhotelItem
from math import ceil
import datetime
from wangModel.utils.mysqlConn import getRows,insert

class TuniuHotelSpider(scrapy.Spider):
    name = 'tuniu_hotel'
    allowed_domains = ['tuniu.com']
    start_urls = ['https://s.tuniu.com/search_complex/hotel-nn-0-%E6%A1%82%E6%9E%97/']
    page = 1
    count = 0
    pageNum=0
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)

    data = {"primary": {"cityCode": "705",
                        "cityType": 0,
                        "checkIn": str(today),
                        "checkOut": str(tomorrow),
                        "roomNum": 1,
                        "adultNum": 2,
                        "childNum": 0,
                        "childAges": [],
                        "keyword": ""},
            "secondary": {
                "poi": {
                    "locationType": 2,
                    "pois": []},
                "prices": [],
                "stars": [],
                "brands": [],
                "features": [],
                "facilities": [],
                "commentScore": "",
                "bedTypes": []},
            "threeStages": [],
            "suggest": {},
            "pageNo": 1,
            "pageSize": 10,
            "sort": 0,
            "customerClient": 2,
            "returnDistance": True,
            "secondaryDist": {"pValue": "", "userType": 0}}
    def start_requests(self):

        url = "https://hotel.tuniu.com/hotel-api/hotel/list?c=%7B%22ct%22%3A20000%7D"
        # url = '	https://hotel.tuniu.com/hotel-api/hotel/detail?c={"ct":20000}&d={"hotelId":"351748651"}'

        yield JsonRequest(
            url=url,
            callback=self.parse,
            data=self.data,
        )

    # 酒店列表数据
    def parse(self, response):
        print(f"爬取第{self.page}页")
        data = response.json()
        # print(data)
        item = TuniuhotelItem()
        self.count = data['data']['count']
        hotellist = data['data']['hotels']
        for i in range(len(hotellist)):
            hotel = hotellist[i]['hotel']
            refer = hotellist[i]['reference']
            item['id'] =hotel['hotelId']
            item['hname'] = hotel['chineseName']
            item['starname'] = hotel['starName']
            item['hpic'] = hotel['firstPic']
            item['haddress'] = hotel['address']
            item['business'] = hotel['business']
            item['distance'] = refer['distanceText']
            item['hlowstprice'] = hotellist[i]['lowestPrice']
            comment = hotellist[i]['comment']


            ##爬取有评论的酒店内容信息
            if 'score' in comment:
                # print("有评论内容",comment)
                hotel_name = str(item['hname']).replace("（", "(").replace("）", ")")
                # print("原始酒店名称", hotel_name)
                sql = "select id,name from hotels where name = %s"
                dataRows=getRows(sql,hotel_name)
                print("数据库的数据查询结果",dataRows)
                print("酒店id",item['id'])
                if dataRows:
                    id = getRows(sql, hotel_name)[0][0]
                    baseName = getRows(sql, hotel_name)[0][1]
                    print("开始爬取酒店：",baseName)
                    yield scrapy.Request(
                        url=f"https://hotel.tuniu.com/hotel-api/comment/summary?c=%7B%22ct%22:20000%7D&d=%7B%22hotelId%22:%22{item['id']}%22%7D",
                        callback=self.parse_summary_comments,
                        dont_filter=False,
                        meta={"hotelId":id,"hotelName":baseName,"item":item}
                    )

            # print(item)
        self.pageNum = ceil(self.count / 10)
        print("总页数", self.pageNum)

        #酒店列表翻页
        if (self.pageNum > 1):
            self.page=self.page+1
            print(f"开始爬取第{self.page}页")
            self.data['pageNo']= self.page
            print(self.page)
            # if(self.page<=self.pageNum):
            if(self.page<=self.pageNum):
                yield JsonRequest(
                    url="https://hotel.tuniu.com/hotel-api/hotel/list?c=%7B%22ct%22%3A20000%7D",
                    callback=self.parse,
                    data=self.data,
                )
                time.sleep(2)

    #评论取出其他类型评论
    def parse_summary_comments(self, response):
        item=response.meta.get('item')
        # print(item)
        id=response.meta.get('hotelId')
        hotelName=response.meta.get('hotelName')
        summary=response.json()
        otherComment=summary['data']['aspects']
        commentSum=summary['data']['commentCount']
        print("爬取分类的评论",otherComment)
        item['others']=otherComment
        item['hcomments']=[]
        requestbody = {
            "hotelId": str(item['id']),
            "grade": "ALL",
            "pageNo": 1,
            "pageSize": 8
        }
        pages=ceil(commentSum/8)
        for i in range(1,pages+1):
            requestbody['pageNo']=i+1
            time.sleep(3)
            yield JsonRequest(
                url="https://hotel.tuniu.com/hotel-api/comment/list?c=%7B%22ct%22%3A20000%7D",
                callback=self.parse_comments,
                dont_filter=False,
                data=requestbody,
                meta={"hotelId": id, "hotelName": hotelName, "item": item,"body":requestbody,"pages":pages,"currentPage":i}
            )
        # yield item
    # 酒店评论内容详情解析
    def parse_comments(self, response):
        # print("进入解析",response)
        item = response.meta.get('item')
        pages = response.meta.get('pages')
        currentPage = response.meta.get('currentPage')
        print(f"解析{item['hname']}第{currentPage}页,共{pages}页")
        data=response.json()
        print("json数据",data)
        id = response.meta.get('hotelId')
        others=item['others']

        otherslist=[]
        # print("其他评论详情",others)
        for contentInfo in others:
            # print(type(contentInfo))
            # print(contentInfo)
            categroy = {}
            categroy["cnName"]=contentInfo['cnName']
            categroy["enName"]=contentInfo['enName']
            categroy["score"]=str(contentInfo['aspectScore'])
            otherslist.append(categroy)
        # print("其他评论", otherslist)
        hotelName = response.meta.get('hotelName')
        comment_sum=data['data']['groupCount']['ALL'] #总评论数
        good=data['data']['groupCount']['GOOD']
        middle=data['data']['groupCount']['COMMON']
        bad=data['data']['groupCount']['BAD']
        sql="insert into hotel_comment(hotelId,hotelName,num,good,middle,bad,othersComment,siteFrom,crawlTime) select %s,%s,%s,%s,%s,%s,%s,%s,%s from dual where not exists (select hotelName,siteFrom,crawlTime from hotel_comment where hotelName= %s and siteFrom='途牛' and crawlTime=%s);"
        insert(sql,(id,hotelName,comment_sum,good,middle,bad,str(otherslist),"途牛",datetime.date.today(),hotelName,datetime.date.today()))
        if 'comments' in data['data']:
            print(data['data']['comments'])
            item['hcomments']=item['hcomments']+data['data']['comments'] #本也评论列表内容
            if currentPage==pages:
                 print( item['hcomments'])
                 yield item


