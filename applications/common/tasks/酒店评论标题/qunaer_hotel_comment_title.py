import requests
import re
import aiohttp
import asyncio
import os
import xlwt
import xlrd
import time
import openpyxl
import json
from datetime import date, timedelta

today = time.strftime("%Y-%m-%d",time.localtime())
tomorrow = (date.today() + timedelta(days= 1)).strftime("%Y-%m-%d")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    # 'Content-Type': 'application/json;charset=utf-8',
    # 'Content-Length': '1418',
    # 'Origin': 'https://hotel.qunar.com',
    # 'Connection': 'keep-alive',
    # 'Referer': 'https://hotel.qunar.com/cn/guilin/?fromDate=2022-11-16&toDate=2022-11-17&cityName=%E6%A1%82%E6%9E%97',
    # 'Cookie': 'QN1=00009180306c48f75230434f; QN300=s%3Dbaidu; QN99=7930; QunarGlobal=10.67.197.57_-315863c_1844fb4402c_-4886|1667785799221; QN205=s%3Dbaidu; QN277=s%3Dbaidu; _i=ueHd8Zy9S8X7Cs5y-nPVKDLNsGkX; QN601=fc3340e635beebd8fed01d244dfa103f; QN269=7D87F9C05E3E11ED8278FA163EAD537B; QN48=tc_b56d9b243d79884d_1844fc7bd55_d0d9; fid=ab2cfc1a-4442-4996-8058-95e369865862; csrfToken=vwiqxqLdRWrdSUvmIn84yliNXbhGLphE; QN58=1668514571680%7C1668514571680%7C1; QN57=16678736048620.2656904960064569; ariaDefaultTheme=null; ctt_june=1654604625968##iK3wVRvNVhPwawPwa%3DjnWRa%2BES2Aa2PwW2aOaS0RE2DsEDGDE2DsERfIXSX8iK3siK3saKjOWst%2BWR3sWRX8VuPwaUvt; ctf_june=1654604625968##iK3wWKDOWuPwawPwasiGXKtmaRamVKGDEDkIVKD%3Da%3DjNX2ERaK3sWDfGX2EDiK3siK3saKjOVRPmVK3wVKaAWwPwaUvt; cs_june=9272ae1939d58083d4743676507ffd29fbabe527912f2f1973ed8370a47566c8150e2f38a8a12ca96514b111ebdac1878f7fa30cb8f280132faaa5b783ecd9d7b17c80df7eee7c02a9c1a6a5b97c117928b56a71cbfdbdae6d0a8e0c2d26aa9e5a737ae180251ef5be23400b098dd8ca; QN271AC=register_pc; QN271SL=791c41e753d68b5ac9365b726bb2960d; QN271RC=791c41e753d68b5ac9365b726bb2960d; _q=U.cbkbblv3519; _s=s_3IDSC2V3W3PGZ5F7A2NNNVAAOE; _t=27907349; _v=SsLO8uhOBBxdqVHEaJ4HRRRm-S5OQ4tF_8od6DDnWkVT_ugYFgt4T06vA1JNPsidy87-YU6-Em7O13wYNxUWwYMcqZtXVYqS6D-UDVREDpp4GBSmQBKSBqR41pOUqtVzJOa7ynWOtM4YS0MiDWncGOrqjfjDGrH8PuPitoHSVLH6; QN43=2; QN42=%E5%8E%BB%E5%93%AA%E5%84%BF%E7%94%A8%E6%88%B7; _vi=CGXWRmr0v6gQkJRlZ_6pw-bLocEdRkSo8Xwow4GZOzimn0tLx6x5Le1BMu6f87LYgsSfYHgjOFhvVsDnmRqzU0mo-HkSSge-5UpMggzcw6CbOTTb41NX1K04bOsVxvYErsEQ-dxBNHzmnLsMbpTpDhjmYVi-cwQPLk3yyborrCAc; QN233=FreetripTouchin; HN1=v1ecbd83e6109eb406ad7ee9754047124a; HN2=qunuqnuggzkcg; __qt=v1%7CVTJGc2RHVmtYMS9JYkhPaVB5VnNneGMxSHB0MjgxTW0vQk00NXIrc1JyWUdyaFhEeWtUbFBDVUk4ZEE5SUN3MFJ0emtjeUVRdkxQUStzRDdoV0NQT1VuOFlyRFZhOGhaZk9TaVJZS1hDZWtYSjdzbHhUR3dSRDRzOXhKRFlLT01BcFBnR2NBY2VaTnh3N0R6bDF3WE9tK2FjcDVPNG1nMk1DeGRqdFAwdkNuK2FaaEdubkdLSzVVUXptcnZqUmVHQXgxWFZrd0d3S08zQThySnVSYkQ0UT09%7C1668589224247%7CVTJGc2RHVmtYMTljdWtuS3FaQklDS2RDeVJDNUVIT2dHVEt3WURCWXAzZ3pNVGZSWlR5TVltSzNDWlh1aFhNK1NKamk3UG5vU21oN2ZTWnN6RHdGWkE9PQ%3D%3D%7CVTJGc2RHVmtYMTlMTFFGQnNtQlVzWUhYeUg1Wnl1WVpMalNYYTlTd3pLZHVmZ0Q2eDNXY1N3VWwwbkZTZEpndnlqeENQcDVSZFlvaFpWVHVXYld4UFh2TVo1TDFPaFJCQndSbDVZWEZUZ3U2SVJwam80cUNYZ0s4VFl3WUpXbzczQjg3TDJmL0x6NnFraDlOdTFoWG1YdVExRjh6ZlBHWGU3WWNjUFNacmJBaURKeGNjdzVVZ3plTndOL0JXekt6T0h5TXQzbGxhVGZjbFRnNFlQMUpLd3ppZHMzQlpBVzlpRmo1WkVHWDVrcDJRZHNYQmRYVTk2eFJiMVZ6cmtpMGFOTHBBVzNBbGhBWEEwZFBjOUNyekl1VGxtUlNyZ09Gc2tZa2F5dnZtS1B2emlLS2VKaFdIVXp6V21vVFhoMmRPby9sa2JVUGZ0enFZREl5bFVrME5RMVM2U1U5eFJIQjdFaCtsZ2dXT3NCWnltelpCYVZxeVVScHhWOXVNakwvd0xqVmZqT1dZZzRrUi9XanUrcTZqYlBrQWRkbHppYVUzejE1Vzg4UTBXS1oyL0lpVmtZQmNEVGVHdjBWdXNSZmw2VUtTeWRKS3VnSXBFZ3A5YmRDRWNvSWpBR3NpM2hwN2JITks0c051S2FuVC9xdGhmdjN0V1JUWUZoRWNkL092aXVqdjFuTktlZUNXa3BvSEdUSklFT0RrVVFsRldPSjdJemlDbm1RUkFkVWdEQk5ib2svZmNzQnpDUjJjOTJoMVdUanE2KytZS24vOVU0dlhGOXMvdDc1NnlVYUhub3pDZnhMQ0k1QTRUbStTMjlpNG9lSm9hd3FGTW1aeWdFRUs0OWhKZVE1c2tiZVJRL2IydkgvVmNlbmRRNTNVeVpKdkxyaFZqbjIxQVZ3Q0FKWFdmTU5XYVp4c0QrQUtmM2M%3D; SECKEY_ABVK=n0yGYaC0Uv/VO8QaVoB7LWOTFI1iG4L4ZC9VsTH65IM%3D; BMAP_SECKEY=yzvwj4ltTTURWnc-Y3gwGTG9ua0QoKNAekMiwcrQ6JAAewWk9khA6I8hsY9M6VR656LUBVS30ubB-smmXJ5vg3QAHYFamo-SGOzGHPzX10oqjUcmL7xZKw-IyJc7cEhRaug23EssK3-RhsYVSss7Ui3jjCW6AxSlVUe3Dz4v2hKyrifgZOqQQOOZ_uacKXiG; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; QN44=cbkbblv3519; QN267=0531040383a985e0a; QN163=0; QN271=2339fa3a-72a3-4cfd-8f88-55e9645bcb62; tabIndex=0; cityUrl=guilin; cityName=%25E6%25A1%2582%25E6%259E%2597; checkInDate=2022-11-16; checkOutDate=2022-11-17',
}

from MysqlConnect import *
mysql = MysqlConnect()

class Qunaer_Hotel:
    async def getComment(self,item, session):
        try:
            async with session.get(item['url']) as res:
                resp = await res.json()
                goodcomment = resp['data']['ratingStat']['positiveCount']
                midcomment = resp['data']['ratingStat']['neutralCount']
                badcomment = resp['data']['ratingStat']['negativeCount']
                count = resp['data']['count']
                othersComment = ""
                args = (item["id"], item["name"], count, goodcomment, midcomment, badcomment, othersComment, today, "去哪儿")
                print(args)
                sql = 'INSERT INTO hotel_comment(hotelId,hotelName,num,good,middle,bad,othersComment,crawlTime,siteFrom) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                mysql.insert(sql, args)
        except Exception as e:
            print("comment报错",e)

    # 从数据库获取酒店信息
    async def getHotel(self):
        async with aiohttp.ClientSession(headers=headers) as session:
            # 从数据库拿url
            results = mysql.queryHotel("select id,name,gw_url from hotels where gw_url!='' and 1000<id ", None)
            tasks = []
            url_list = []
            for row in results:
                id = row[0]
                name = row[1]
                url = row[2]
                url_list.append({
                    "id": id,
                    "name": name,
                    "url": url,
                })
            print("去哪儿网站的所有酒店长度", len(url_list))
            i = 0
            for item in url_list:
                task2 = asyncio.create_task(self.getComment(item, session))
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
