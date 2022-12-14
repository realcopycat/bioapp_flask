import requests
import re
import aiohttp
import asyncio
import csv
import json
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
    'Cookie':"_bfa=1.1667787832924.3h7rvk.1.1669895769722.1669970415585.59.1057.0; _ubtstatus=%7B%22vid%22%3A%221667787832924.3h7rvk%22%2C%22sid%22%3A59%2C%22pvid%22%3A1057%2C%22pid%22%3A0%7D; MKT_OrderClick=ASID=4897155952&AID=4897&CSID=155952&OUID=index&CT=1669895769884&CURL=https%3A%2F%2Fwww.ctrip.com%2F%3Fsid%3D155952%26allianceid%3D4897%26ouid%3Dindex&VAL={}; __zpspc=9.66.1669970417.1669972201.47%232%7Cwww.baidu.com%7C%7C%7C%25E6%2590%25BA%25E7%25A8%258B%25E6%2594%25BB%25E7%2595%25A5%7C%23; _jzqco=%7C%7C%7C%7C1669970417342%7C1.386356559.1667787833232.1669971673086.1669972201783.1669971673086.1669972201783.undefined.0.0.519.519; MKT_CKID=1667787833303.6cihj.yc0k; _RF1=180.136.89.152; _RSG=PI4tVah22dC4DYKmrdfaUA; _RDG=28a682bf6ceb192ebc37d846ca69b5ed63; _RGUID=c9c20ab9-1fdc-4499-a7a4-a67d70522344; MKT_Pagesource=PC; _bfaStatusPVSend=1; _bfaStatus=success; nfes_isSupportWebP=1; _ga=GA1.2.728287556.1667875987; Session=SmartLinkCode=ctrip&SmartLinkKeyWord=&SmartLinkQuary=_UTF.&SmartLinkHost=ctrip.com&SmartLinkLanguage=zh; UUID=20EDDDB8AE46403495EFEE36FAC417C1; IsPersonalizedLogin=F; ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; ibu_h5_lang=en; ibu_h5_local=en-us; Hm_lvt_37b54c42b9dde393e60c88c1a84657cb=1668156071,1668390905,1668766327,1669630249; _lizard_LZ=ghjTSPinRlQVIkJmqrUWXFopstucvwx210a3ydz754YfM6ZE89+b-eKCHOLNBGAD; intl_ht1=h4=33_75424975,33_782288,33_6550062,2_441618; _abtest_userid=294c1513-b267-4324-8a01-750ac3d84f81; _gcl_au=1.1.920354234.1668409170; U_TICKET_SELECTED_DISTRICT_CITY=%7B%22value%22%3A%7B%22districtid%22%3A%222%22%2C%22districtname%22%3A%22%E4%B8%8A%E6%B5%B7%22%2C%22isOversea%22%3Anull%7D%2C%22createTime%22%3A1668416843913%2C%22updateDate%22%3A1668416843913%7D; FlightIntl=Search=[%22KWL|%E6%A1%82%E6%9E%97(KWL)|33|KWL|480%22%2C%22BJS|%E5%8C%97%E4%BA%AC(BJS)|1|BJS|480%22%2C%222022-11-17%22]; Hm_lvt_576acc2e13e286aa1847d8280cd967a5=1668916753; Union=OUID=index&AllianceID=4897&SID=155952&SourceID=&createtime=1669895770&Expires=1670500569884; login_uid=C0AB45AFF50D550863B877680E735ABE; login_type=0; cticket=337E22BDC21DD4985842195D8CEDEC0CE79886C069743562391907D8E4575607; AHeadUserInfo=VipGrade=0&VipGradeName=%C6%D5%CD%A8%BB%E1%D4%B1&UserName=&NoReadMessageCount=0; DUID=u=C0AB45AFF50D550863B877680E735ABE&v=0; IsNonUser=F; appFloatCnt=1; StartCity_Pkg=PkgStartCity=33; GUID=09031172114453342165; _bfs=1.61; MKT_CKID_LMT=1669970417053; _bfi=p1%3D290570%26p2%3D290601%26v1%3D1056%26v2%3D1055"
}
from datetime import date, timedelta

today = time.strftime("%Y-%m-%d", time.localtime())
tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
from MysqlConnect import *

mysql = MysqlConnect()


# 爬取评论标题
class Xiecheng_Route:
    async def getCommentTitle(self,item, session):
        data = json.loads(item['data'])
        try:
            async with session.post(item['url'], json=data) as res:
                dic = {}
                otherComment = []
                resp = await res.json()
                commentAggregation = resp['commentAggregation']
                totalCount = resp['totalCount']
                scoreAvg = commentAggregation['scoreAvg']
                goodRate = commentAggregation['goodRate']
                commonTags = commentAggregation['commonTags']
                dic['score'] = scoreAvg
                dic['goodRate'] = goodRate
                dic['total'] = totalCount
                for comment in commonTags:
                    totalCount = comment['totalCount']
                    displayName = comment['displayName']
                    if displayName == '好评' or displayName == '中差评':
                        dic[f'{displayName}'] = totalCount
                    else:
                        otherComment.append({f'{displayName}': totalCount})
                if 'tourTypeTags' in commentAggregation:
                    tourTypeTags = commentAggregation['tourTypeTags']
                    for comment in tourTypeTags:
                        totalCount = comment['totalCount']
                        displayName = comment['displayName']
                        otherComment.append({f'{displayName}': totalCount})
                if 'aiTags' in commentAggregation:
                    aiTags = commentAggregation['aiTags']
                    for comment in aiTags:
                        totalCount = comment['totalCount']
                        displayName = comment['displayName']
                        otherComment.append({f'{displayName}': totalCount})
                if 'subItemTags' in commentAggregation:
                    subItemTags = commentAggregation['subItemTags']
                    for comment in subItemTags:
                        totalCount = comment['totalCount']
                        displayName = comment['displayName']
                        otherComment.append({f'{displayName}': totalCount})
                args = (
                item['id'], item['name'], dic['total'], dic['score'], dic['goodRate'], dic['好评'], dic['中差评'], dic['中差评'],
                str(otherComment), today, "携程")
                print(args)
                sql = 'INSERT INTO route_comment(route_id,route_name,total,score,goodRate,good,middle,bad,othersComment,crawlTime,siteFrom) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                mysql.insert(sql, args)
        except Exception as e:
            print("comment报错", e)
            print(resp)

    async def getRoute(self):
        async with aiohttp.ClientSession(headers=headers) as session:
            # results = mysql.query("select id,route_name,xc_url,xc_data from route where xc_data !='' and id  = 106", None)
            results = mysql.query("select id,route_name,xc_url,xc_data from route where xc_data !=''", None)
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
            print("携程网站的所有线路长度", len(url_list))
            # print(url_list)
            i = 0
            for item in url_list:
                task = asyncio.create_task(self.getCommentTitle(item, session))
                i = i + 1
                tasks.append(task)
                if i % 10 == 0:
                    time.sleep(5)
                await asyncio.wait(tasks)
            # 关闭mysql
            mysql.cur.close()
            mysql.connection.close()

if __name__ == '__main__':
    asyncio.run(getScenic())
