import requests
import re
import aiohttp
import asyncio
import csv
import json
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
    # 'Referer': "https://glsh7.package.qunar.com/user/detail.jsp?id=3078148931&osrc=tts_tuan&rttp=%E6%9C%AC%E5%9C%B0%E6%B8%B8&dep=5qGC5p6X&arr=5qGC5p6X&ftdt=2023-03-01%2C2023-03-01&qssrc=eyJ0cyI6IjE2Njk4NzM1MTgyMzUiLCJzcmMiOiJ1bmRlZmluZWQuZW52YW5vIiwiYWN0Ijoic2Nyb2xsIiwicmFuZG9tIjoiOTU1MjAwIn0=",
    # 'Cookie': "QN1=00009180306c48f75230434f; QN300=s%3Dbaidu; QN99=7930; QunarGlobal=10.67.197.57_-315863c_1844fb4402c_-4886|1667785799221; QN205=s%3Dbaidu; QN277=s%3Dbaidu; _i=ueHd8Zy9S8X7Cs5y-nPVKDLNsGkX; QN601=fc3340e635beebd8fed01d244dfa103f; QN269=7D87F9C05E3E11ED8278FA163EAD537B; QN48=tc_b56d9b243d79884d_1844fc7bd55_d0d9; fid=ab2cfc1a-4442-4996-8058-95e369865862; csrfToken=vwiqxqLdRWrdSUvmIn84yliNXbhGLphE; QN58=1669821195055%7C1669822256665%7C5; QN57=16678736048620.2656904960064569; ctt_june=1654604625968##iK3wVRvNVhPwawPwa%3DjnWRa%2BES2Aa2PwW2aOaS0RE2DsEDGDE2DsERfIXSX8iK3siK3saKjOWst%2BWR3sWRX8VuPwaUvt; ctf_june=1654604625968##iK3wVK3OaUPwawPwas2sXsjNXs2mWSXnXPEIaRHIaPX8X%3DDOaRanXPEhEPjAiK3siK3saKjOVKjsaSaAas38ahPwaUvt; cs_june=173605640a003a620f2f106b211063ea2287c94e80d66389452136307aa6d7d9150e2f38a8a12ca96514b111ebdac1878f7fa30cb8f280132faaa5b783ecd9d7b17c80df7eee7c02a9c1a6a5b97c117951bd5a81c5254ab3bab7748a9aa6d8185a737ae180251ef5be23400b098dd8ca; QN271AC=register_pc; QN271SL=791c41e753d68b5ac9365b726bb2960d; QN271RC=791c41e753d68b5ac9365b726bb2960d; _q=U.cbkbblv3519; _s=s_3IDSC2V3W3PGZ5F7A2NNNVAAOE; _t=27907349; _v=SsLO8uhOBBxdqVHEaJ4HRRRm-S5OQ4tF_8od6DDnWkVT_ugYFgt4T06vA1JNPsidy87-YU6-Em7O13wYNxUWwYMcqZtXVYqS6D-UDVREDpp4GBSmQBKSBqR41pOUqtVzJOa7ynWOtM4YS0MiDWncGOrqjfjDGrH8PuPitoHSVLH6; QN43=2; QN42=%E5%8E%BB%E5%93%AA%E5%84%BF%E7%94%A8%E6%88%B7; _vi=CxIUDXSKKXrdfKW8a_JOt7FdAzF3YVARuSGejExpLtNTYJb0IsR-5f82yRcybhrWWwl3aU7KqT10nKk_ydXwYxMzUiLL1hgdynGc4YfMr2UYeME-S_UnXUKnHzth2xeCRbsBgBPNuA-aM44OzN_1OoHFpGGhOCYcEmmLrjtCInJi; QN233=FreetripTouchin; HN1=v1ecbd83e6109eb406ad7ee9754047124a; HN2=qunuqnuggzkcg; quinn=e5ba94e400db7ae611b28097b8ad7ddc9fea18aa074280921e89258cf82e7cb417cc1fc89ba3f04bfda0535faf80ae42; QN621=1490067914133%2Ctestssong%3DDEFAULT%26fr%3Dtejia_inton_search%261490067914133%252Ctestssong%3DDEFAULT; QN668=51%2C56%2C56%2C58%2C56%2C55%2C54%2C56%2C58%2C57%2C57%2C51%2C56; QN243=572; _jzqa=1.2488123552548573700.1668855923.1669870580.1669874997.8; _jzqx=1.1669087498.1669874997.1.jzqsr=dujia%2Equnar%2Ecom|jzqct=/.-; ariaDefaultTheme=null; QN100=WyLmoYLmnpfpmLPmnJTnuq%2FnjqnkuIDml6XmuLjpk7blrZDlsqnml6DotK3nial85qGC5p6XIiwi54Ot6I2QMTLkurrnsr7lk4HlsI%2Flm6Ig5ryT5rGf5ri46Ii5MjDlhYPog4zmma%2FpgYfpvpnmsrPpk7blrZDlsqnljYF85qGC5p6XIiwi5qGC5p6XfOahguaelyJd; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; QN44=cbkbblv3519; QN267=053104038b8bcf1fd; QN163=0; QN271=638b35df-ba09-4ab7-a0ef-e80528529e59; _jzqc=1; _jzqckmp=1; QN61=%5B%22%E6%A1%82%E6%9E%97%E9%98%B3%E6%9C%94%E7%BA%AF%E7%8E%A9%E4%B8%80%E6%97%A5%E6%B8%B8%E9%93%B6%E5%AD%90%E5%B2%A9%E6%97%A0%E8%B4%AD%E7%89%A9%22%2C%22%E7%83%AD%E8%8D%9012%E4%BA%BA%E7%B2%BE%E5%93%81%E5%B0%8F%E5%9B%A2%20%E6%BC%93%E6%B1%9F%E6%B8%B8%E8%88%B920%E5%85%83%E8%83%8C%E6%99%AF%E9%81%87%E9%BE%99%E6%B2%B3%E9%93%B6%E5%AD%90%E5%B2%A9%E5%8D%81%22%2C%22%E6%A1%82%E6%9E%97%22%5D; _qzja=1.621578797.1669870580293.1669870580293.1669875028328.1669876047449.1669877523855..0.0.7.2; _qzjc=1; _qzjto=7.2.0; Hm_lvt_a8a41d37454fd880cdb23d6ef05d917b=1669870580; Hm_lpvt_a8a41d37454fd880cdb23d6ef05d917b=1669877524; JSESSIONID=A0CB91CD362911D601F4C9CF6971DF8D; activityClose=1; _jzqb=1.24.10.1669874997.1; _qzjb=1.1669875028328.3.0.0.0"
}
from datetime import date, timedelta

today = time.strftime("%Y-%m-%d", time.localtime())
tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
from MysqlConnect import *

mysql = MysqlConnect()

class Qunaer_Route:
    # 爬取评论标题
    async def getCommentTitle(self,item, session):
        data = json.loads(item['data'])
        try:
            async with session.post(item['url'],data=data) as res:
                otherComment = []
                resp = await res.json()
                # print(resp)
                resp = resp['data']
                totalComment = resp['totalComment']
                ratingExcellent = resp['ratingExcellent']
                ratingAverage = resp['ratingAverage']
                ratingAwful = resp['ratingAwful']
                numWithImages = resp['numWithImages']
                goodRate = 0
                if totalComment != 0:
                    goodRate = ratingExcellent/totalComment
                otherComment.append({'有图':numWithImages})
                # mainCommentList = resp['mainCommentList']
                args = (
                item['id'], item['name'], totalComment, 0, goodRate, ratingExcellent, ratingAverage, ratingAwful,
                str(otherComment), today, "去哪儿")
                print(args)
                sql = 'INSERT INTO route_comment(route_id,route_name,total,score,goodRate,good,middle,bad,othersComment,crawlTime,siteFrom) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                mysql.insert(sql, args)
        except Exception as e:
            print("comment报错", e)
            print(resp)
            # time.sleep(3)
            # async with aiohttp.ClientSession(headers=headers) as session1:
            #     await getCommentTitle(item,session1)

    async def getRoute(self):
        # results = mysql.query("select id,route_name,xc_url,xc_data from route where xc_data !='' and id  = 106", None)
        results = mysql.query("select id,route_name,gw_url,gw_data from route where gw_data !=''", None)
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
        tasks = []
        print("去哪儿网站的所有线路长度", len(url_list))
        # print(url_list)
        i = 0
        for item in url_list:
            async with aiohttp.ClientSession(headers=headers) as session:
                task = asyncio.create_task(self.getCommentTitle(item, session))
                i = i + 1
                tasks.append(task)
                if i % 2 == 0:
                    time.sleep(5)
                await asyncio.wait(tasks)
        # 关闭mysql
        mysql.cur.close()
        mysql.connection.close()

if __name__ == '__main__':
    # test()
    # asyncio.run(getSearch())
    asyncio.run(getScenic())
