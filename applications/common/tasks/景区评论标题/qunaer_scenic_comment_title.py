import requests
import re
import aiohttp
import asyncio
import os
import xlwt
import xlrd
import time
import random
import json
import openpyxl

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
    "Cookie": 'SECKEY_ABVK=6HIqXjD0ds/vRQnCLt0mHL+BlKCMeW1C20QspZholGg%3D; BMAP_SECKEY=OwZJJ1XtuED6yxVKpYWTZlTrTfswjB7iLK1DDxx5laDPIMT285FwiY4kkMQRbmC-Qa_BYY2jMWeW6YXOu2TQBUSKqwawAnndWCRQARf00Hr7hN3NWtO8bePrI84I1wO0XUK8Bk2BjsTKbFG-9C7uvg-ijL9UVeXTY9x8XC1q_JuGPhwYESA4uJipuwkX1kLC; QN1=00009180306c48f75230434f; QN300=s%3Dbaidu; QN99=7930; QunarGlobal=10.67.197.57_-315863c_1844fb4402c_-4886|1667785799221; QN205=s%3Dbaidu; QN277=s%3Dbaidu; _i=ueHd8Zy9S8X7Cs5y-nPVKDLNsGkX; QN601=fc3340e635beebd8fed01d244dfa103f; QN269=7D87F9C05E3E11ED8278FA163EAD537B; QN48=tc_b56d9b243d79884d_1844fc7bd55_d0d9; fid=ab2cfc1a-4442-4996-8058-95e369865862; csrfToken=vwiqxqLdRWrdSUvmIn84yliNXbhGLphE; QN67=4815%2C8402%2C461%2C6287%2C31980%2C6675%2C39170%2C514011%2C513120%2C512329; QN58=1668915779477%7C1668915787448%7C4; QN57=16678736048620.2656904960064569; Hm_lvt_15577700f8ecddb1a927813c81166ade=1668508423,1668670982,1668768828,1668852847; ctt_june=1654604625968##iK3wVRvNVhPwawPwa%3DjnWRa%2BES2Aa2PwW2aOaS0RE2DsEDGDE2DsERfIXSX8iK3siK3saKjOWst%2BWR3sWRX8VuPwaUvt; ctf_june=1654604625968##iK3wWKXmWUPwawPwasXwaRj8VKiGVRiTWKg%3DERjNES2OXsDwaRPsEKasWPPsiK3siK3saKjOVRtOVRjmWsamWhPwaUvt; cs_june=84ca3a9b5a98782f34be6296a1606f06eb95a586e457de9dc68fac6e9a429296150e2f38a8a12ca96514b111ebdac1878f7fa30cb8f280132faaa5b783ecd9d7b17c80df7eee7c02a9c1a6a5b97c1179abfc7c950e9b30934146fcf8bd089a765a737ae180251ef5be23400b098dd8ca; QN271AC=register_pc; QN271SL=791c41e753d68b5ac9365b726bb2960d; QN271RC=791c41e753d68b5ac9365b726bb2960d; _q=U.cbkbblv3519; _s=s_3IDSC2V3W3PGZ5F7A2NNNVAAOE; _t=27907349; _v=SsLO8uhOBBxdqVHEaJ4HRRRm-S5OQ4tF_8od6DDnWkVT_ugYFgt4T06vA1JNPsidy87-YU6-Em7O13wYNxUWwYMcqZtXVYqS6D-UDVREDpp4GBSmQBKSBqR41pOUqtVzJOa7ynWOtM4YS0MiDWncGOrqjfjDGrH8PuPitoHSVLH6; QN43=2; QN42=%E5%8E%BB%E5%93%AA%E5%84%BF%E7%94%A8%E6%88%B7; _vi=vngppYwRPwCDqhIqFPtxLm89wykxl2K7lGZEPOnwB341RCRAj3afnxLN-pQ2n-drX7GENqb0dVOcAFO7QBxpE7uqmso_3vMGM223wBq9FSP8OX21p_a6qwYhay-zJs3uYLRjvOLn0RpM-D8_YQGmyG5ba2uC3XqyN76edIKIa709; QN233=FreetripTouchin; __qt=v1%7CVTJGc2RHVmtYMStSdWh2QnF2amE0bVovaEEzaFVaK0pTaTcrdkIzRWd6VGx1V2xGUWtLMFZwdEFqRzBVMncvd0dqbEJhMXFTZk1FUFN6M3drN2tSR0MzMzUveURkN09yZUJ6dWVkQ2VvanJDRWZYTTh5L0NYUFN1YlMydVJJMVRDVEtNZmxyQWRiTEdiVUU1ZVp1UW5xQWtHbmhTbk1NZGR3Z2tKK0lrbWFudDkvVmVxZzFsL3NLVUt1Y1dsU0N5bERITnVRM2hlN1NDbSt0TGphTnZROUVJOWdBbmNXSDNRYUpzZHBhYURLdz0%3D%7C1668915783978%7CVTJGc2RHVmtYMS9Va284c1RyZGtEOFlGUXZlUWdveFFmdGdJNWwyTHlaSVlNYWorNlF5dmJ5eTAxaUhGZ1BId3VVZFJ2RnJQRk9oUW9jVnFhenVoYXc9PQ%3D%3D%7CVTJGc2RHVmtYMThzTUJOUVkzeUErMkpQMi9vT1dSN2Zib20zaUdOeWUwQ3BHWHBldWw1dld3YWhmdCtiQ3NZbFBiTERyYkdiMnhVYlhKdmQ1Wk5MNHFyQUEzSThWKzZTMHAyQndlYWtWQVplM2hlSkY5WXVxR2Iva1VwRWsrakEvdUttcXpnYWgrVys2REVvVVVMdm9tcDJ4OGpWdDlMUHZCT2pHMndub1VVM2doRHdTdnNudjBjdS9peXNiUkFxMVc1czlmTU56b2NNR3pqZEl5Ulc4RE94VmtLMFlDWlNnWEdGVVNTaVB3YVpYZnF6ZzIwdGxmVG5xUEhzZXJVZXk1UjdFbzFnRXhCa0I4MENLOEhBdE82azlpWCs2dlkwa092Q3dsMjExYTVDSlptY3BPdm1raVpMVytoT3dEMm52Y1ZyMEY2cVBER240c2Z4MDZrcFFOL3NTVFhMcm1IZlorT2U3RFJ1d1ltTmsvem91Kyt5TDdQOEVLZGQwOVVTVnl4QkcwbmEwcGo2T1lXc0U4c3l0UzlMY1k0bGpNc1lMSkVKODNkMVdPdzdJUklZYnE0eDdyYVVETU9nV2NTNTlHenRJS1ROZ3VvYXBocGszS0FkZWlZMGNtdWlBVFBzRTFKVTRwVjdCU3EwS2hMeGhqTUtGa1NEOGtkdlEzMS92VHB2MmxENUZ1aEhodEU1K1d5Q2RVL3FzaDhPa2xuUGpsQ0tJc1ZaeGNGL3hRU0NMclVEeXMzbjhvTEZ2RGlZMUE1WVhhUnN5NHkrelp5Sy84S2FYTUtZM0ZNR3A5ZWdqTkdobWlZOWt3T1FodHhuVE1HZ0xuQWI4alhuNkg0WkhLQXM4ZUcwMzlpQ2JFZFRKdFZUajMxMnFqNkpoU1VXZUNaa1dYdDJFWkFwZ1VscFQ0emFvM3d3dFFqQjlGdWlJMDU3aXR2L3BPSU1VRWFGRVQxSi9kV0xzVy9EdzRXVHVCU0NBMFJGaGlNVm5qN1JUMHhIV0VpS1QyWkVIeWF2c3dWTU5iNU1QQytWREh0OG5SRWJwOGE5N1g3OHVYT29ldENmb250OHZMNDVnOUlxdHM0N0IzUmFVMEJ4eitGNUJ1L3pVVXM5WDRZTURlS09SSUNkL3c9PQ%3D%3D; HN1=v1ecbd83e6109eb406ad7ee9754047124a; HN2=qunuqnuggzkcg; quinn=e5ba94e400db7ae611b28097b8ad7ddc9fea18aa074280921e89258cf82e7cb417cc1fc89ba3f04bfda0535faf80ae42; QN621=1490067914133%2Ctestssong%3DDEFAULT%26fr%3Dtejia_inton_search%261490067914133%252Ctestssong%3DDEFAULT; QN668=51%2C56%2C56%2C58%2C56%2C55%2C54%2C56%2C58%2C57%2C57%2C51%2C56; ariaDefaultTheme=null; QN63=%E6%A1%82%E6%9E%97%7C%E9%87%8D%E5%BA%86%7Cgl%20%7C%E9%98%B3%E6%9C%94%E5%8A%A8%E6%84%9F6D%E7%94%B5%E5%BD%B1%7C%E4%B8%80%E9%94%8B%E8%B6%8A%E9%87%8E%E5%B1%B1%E5%9C%B0%E8%BD%A6%E4%BF%B1%E4%B9%90%E9%83%A8%7C%E6%A1%82%E6%9E%97%E5%86%9B%E5%8D%9A%E5%9B%AD; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; QN44=cbkbblv3519; QN267=05310403864bcfa85; QN163=0; JSESSIONID=1AD098F421DEEF0CDC162A9D3277ECCE; QN271=a9ec74f7-b22b-4855-9aed-c212fe90a582; QN71="MTgwLjEzNi43MC41MzrmoYLmnpc6MQ=="; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1668915784; QN1231=0; activityClose=1; QN243=15; QN310=hrec_zaj86'
}
# 获取当前时间
from datetime import date, timedelta
today = time.strftime("%Y-%m-%d",time.localtime())
tomorrow = (date.today() + timedelta(days= 1)).strftime("%Y-%m-%d")

from MysqlConnect import *
mysql = MysqlConnect()

class Qunaer_Scenic:
    async def getComment(self,item, index, session,dic,comments):
        try:
            async with session.get(item["url"]) as res:
                resp = await res.json()
                # print(resp)
                dic["score"] = str(resp["data"]["score"])
                dic["commentCount"] = str(resp["data"]["commentCount"])
                dic["好评"] = 0
                dic["中评"] = 0
                dic["差评"] = 0
                # commentList = resp["data"]["commentList"]
                if index == 1:
                    othersComment = []
                    tagList = resp["data"]["tagList"]
                    # print(tagList)
                    for tag in tagList:
                        tagName = tag["tagName"]
                        tagNum = tag["tagNum"]
                        if tagName != "好评" and tagName != "中评"'' and tagName != "差评":
                            othersComment.append({f"{tagName}":tagNum})
                        dic[f"{tagName}"] = tagNum
                    othersComment = str(othersComment)
                    args = (item["id"],item["name"],dic["score"],dic["commentCount"],dic["好评"],dic["中评"],dic["差评"],othersComment,today,"去哪儿")
                    print(args)
                    sql = f'INSERT INTO scenic_comment(scenicId,scenicName,score,num,good,middle,bad,othersComment,crawlTime,siteFrom) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                    mysql.insert(sql,args)
        except Exception as e:
            print("comment报错",e)
            print(item)
            # print("报错页数",index,sightId)

    async def getScenic(self):
        async with aiohttp.ClientSession(headers=headers) as session:
            results = mysql.query("select id,name,gw_url from scenics where gw_url !=''", None)
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
            print("去哪儿网站的所有景区长度",len(url_list))
            i = 0
            for item in url_list:
                dic = {}
                comments = {}
                task1 = asyncio.create_task(self.getComment(item, 1, session, dic, comments))
                i = i + 1
                tasks.append(task1)
                if i % 5 == 0 :
                    time.sleep(5)
                await asyncio.wait(tasks)
            # 关闭mysql
            mysql.cur.close()
            mysql.connection.close()

if __name__ == "__main__":
    asyncio.run(getScenic())
