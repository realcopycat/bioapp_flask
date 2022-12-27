import requests
import re
import aiohttp
import asyncio
import csv
import json
import os
import time
import datetime
import pytz

from datetime import date, timedelta

today = time.strftime("%Y-%m-%d", time.localtime())
tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
headers = {
    'Host': 'www.ly.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'tmapi-client': 'tpc',
    'appfrom': '16',
    'cluster': 'idc',
    'deviceid': 'd0e094a7-a80c-453b-82c5-f593d99e4c35',
    'traceid': '1695c089-9f04-44d6-beb7-41a3689edfd5',
    'Connection': 'keep-alive',
    'Referer': 'https://www.ly.com/hotel/hotellist?pageSize=20&t=1668496948801&city=102&inDate=2022-11-15&outDate=2022-11-16&filterList=8888_1',
    'Cookie': f'SECKEY_ABVK=HszLUR4bbMgPWbGpeaYwbnMzNSB8SbXGhmS9odMd70Q%3D; BMAP_SECKEY=MORm19l7pkFSd3jICPEEe16DM0R-sY9MVVQUmWSB28tD0qRlMBoQwhGvbBs2-1_b7Fyy9msydOvLpZET2XNwl6sdMkCbo0lwHjgDBs4YP2lE5h9fanCHdFch01LvClsY9xYHrOlIMobFBS1Pnzi4cLujgsusthtxVK4YGjGqsQuhPFKwgAf4kuwYIWPxa95u; _dx_uzZo5y=5edb851076e73262f075be8f0ffaaf6e3c2297a4b63d42c5d1d231595a42a46c8cb790a8; Hm_lvt_64941895c0a12a3bdeb5b07863a52466=1668669174,1669038391,1669042695,1669088760; __tctma=144323752.16677878877661.1667787887750.1669092022899.1669095674727.15; H5CookieId=d0e094a7-a80c-453b-82c5-f593d99e4c35; Hm_lvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1668669182,1669038398,1669042705,1669088762; _dx_captcha_cid=06284819; _dx_app_bc4b3ca6ae27747981b43e9f4a6aa769=637b814eXFfcQWGQWFSCEnNPnInDSNFQ3UOJCbJ1; businessLine=hotel; firsttime=1668495014628; lasttime=1669096008415; cityid=2101; nus=userid=819559597&nickName=%e5%90%8c%e7%a8%8b%e4%bc%9a%e5%91%98_59287A06B3A&level=1; __ftoken=sn5o6j2U%2Fr0AktDkUXYquYrYm%2FYg8YzOVtJ%2FplIFl6gQxfOSc%2B8QwfR%2BAan9v4glQv3LdEaLVvDb5I2ukTmy%2Bw%3D%3D; __ftrace=ada97b48-152a-4527-981a-194bd2c90cd3; _tcudid_v2=T1a4qnnExKXGp3YgAYIp90heDDbPN0mtmTQ66BfSVPk; indexTopSearchHistory=%5B%22%E8%B5%84%E6%BA%90%E5%8E%BF%E5%A1%98%E6%B4%9E%E6%99%AF%E5%8C%BA%EF%BC%88%E7%BA%A2%E8%89%B2%E6%99%AF%E5%8C%BA%EF%BC%89%22%2C%22%E8%B5%84%E6%BA%90%E5%8E%BF%E5%AE%9D%E9%BC%8E%E6%99%AF%E5%8C%BA%22%2C%22%E6%A1%82%E6%9E%97%E8%B5%84%E6%B1%9F%E7%81%AF%E8%B0%B7%E6%99%AF%E5%8C%BA%22%2C%22v%22%2C%22%E6%A1%82%E6%9E%97%E8%B5%84%E6%B1%9F%C2%B7%E5%A4%A9%E9%97%A8%E5%B1%B1%E6%99%AF%E5%8C%BA%22%2C%22%E7%BD%97%E6%B1%89%E6%9E%9C%E5%B0%8F%E9%95%87%22%2C%22%E6%B0%B8%E7%A6%8F%E5%8E%BF%E5%87%A4%E5%B1%B1%E6%99%AF%E5%8C%BA%22%2C%22%E6%B0%B8%E7%A6%8F%E9%87%91%E9%92%9F%E5%B1%B1%E6%97%85%E6%B8%B8%E5%BA%A6%E5%81%87%E5%8C%BA%22%2C%22%E7%82%8E%E4%BA%95%22%2C%22%E6%A1%82%E6%9E%97%E6%B9%98%E5%B1%B1%E9%85%BF%E9%85%92%E7%94%9F%E6%80%81%E5%9B%AD%E6%99%AF%E5%8C%BA%22%5D; H5Channel=mnoreferseo%2CSEO; indate=2022-11-22; outdate=2022-11-23; _ga=GA1.2.85011599.1669042102; NewProvinceId=7; NCid=102; NewProvinceName=%E5%B9%BF%E8%A5%BF; NCName=%E6%A1%82%E6%9E%97; 17uCNRefId=RefId=6928722&SEFrom=baidu&SEKeyWords=; TicketSEInfo=RefId=6928722&SEFrom=baidu&SEKeyWords=; CNSEInfo=RefId=6928722&tcbdkeyid=&SEFrom=baidu&SEKeyWords=&RefUrl=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DqMP277Q9_03GFp9XDaOnD1yESxu4dQFrYoLTVLEI2Fa%26wd%3D%26eqid%3Da43766230008598a00000006637c52b4; qdid=39264|1|6928722|0a6c16,39264|1|6928722|0a6c16; route=a14e2b278f3edf5ed22249307678b7ac; __tctmc=144323752.108798340; __tctmd=144323752.737325; __tctmu=144323752.0.0; __tctmz=144323752.1669092022899.14.2.utmccn=(organic)|utmcmd=organic|utmEsl=gb2312|utmcsr=baidu|utmctr=; longKey=16677878877661; __tctrack=0; Hm_lpvt_64941895c0a12a3bdeb5b07863a52466=1669092025; Hm_lpvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1669097452; JSESSIONID=61FD1846F1708452C94F9453B2635172; __sd_captcha_id=b21a6833-60c4-46a2-8d97-1513ef3640ea; searchEntranceId=h5_home; DetailNewOrOld=newDetail; passport_login_state=pageurl=http%3a%2f%2fmember.ly.com%2forder; __tctmb=144323752.3725345079911344.1669097434738.1669097450268.10; tracerid=nologin-1669096963503; ASP.NET_SessionId=4y5ue4pydjihkcjgludpsddw',
}

from MysqlConnect import *
mysql = MysqlConnect()

# 爬取一个酒店的评论
class Tongcheng_Hotel:
    async def getComment(self,item, pageIndex, session):
        data = json.loads(item['data'])
        try:
            async with session.post(item['url'], json=data) as res:
                res1 = await res.json()
                # print(res1)
                # comments = res1['data']['comments']
                filterList = res1['data']['filterList']
                subTags = filterList[0]['subTag']
                dic = {}
                dic["中评"] = 0
                othersComment = []
                for filter in filterList:
                    filterName = filter['filterName']
                    filterCount = filter['filterCount']
                    if filterName == '好评' or filterName == '待改善' or filterName == '全部':
                        dic[f'{filterName}'] = filterCount
                    else:
                        othersComment.append({f"{filterName}": filterCount})
                for subTag in subTags:
                    subTagName = subTag['filterName']
                    subTagCount = subTag['filterCount']
                    othersComment.append({f"{subTagName}": subTagCount})
                othersComment = str(othersComment)
                args = (item["id"], item["name"], dic["全部"], dic["好评"], dic["中评"], dic["待改善"], othersComment,today, "同程")
                print(args)
                sql = f'INSERT INTO hotels(name,level,address,tc_url,tc_data,crawlTime) VALUES(%s,%s,%s,%s,%s,%s);'
                mysql.insert(sql, args)
        except Exception as e:
            print('comment',e)

    # 从数据库获取酒店信息
    async def getHotel(self):
        async with aiohttp.ClientSession(headers=headers) as session:
            # 从数据库拿url
            results = mysql.queryHotel("select id,name,tc_url,tc_data from hotels ", None)
            tasks = []
            url_list = []
            for row in results:
                id = row[0]
                name = row[1]
                url = row[2]
                data = row[3]
                url_list.append({
                    "id": id,
                    "name": name,
                    "url": url,
                    "data": data,
                })
            print("同程网站的所有酒店长度", len(url_list))
            i = 0
            for item in url_list:
                print(item['name'])
                task2 = asyncio.create_task(self.getComment(item, 1, session))
                i = i + 1
                tasks.append(task2)
                if i % 5 == 0 :
                    time.sleep(5)
                await asyncio.wait(tasks)
        # 关闭mysql
        mysql.cur.close()
        mysql.connection.close()

if __name__ == '__main__':
    # saveHotel()
    asyncio.run(getHotel())
