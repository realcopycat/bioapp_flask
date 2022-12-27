import requests
import re
import aiohttp
import asyncio
import csv
import json
import time
from 旅游项目.HBaseConnect import *

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    # 'Accept': 'application/json',
    # 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'P': '41687220417',
    # 'Content-Type': 'application/json;charset=UTF-8',
    # 'Content-Length': '3653',
    # 'Origin': 'https://hotels.ctrip.com',
    # 'Connection': 'keep-alive',
    # 'Referer': 'https://hotels.ctrip.com/',
    'Cookie': '_bfa=1.1667787832924.3h7rvk.1.1670568674517.1670572311780.70.1211.212092; _ubtstatus=%7B%22vid%22%3A%221667787832924.3h7rvk%22%2C%22sid%22%3A70%2C%22pvid%22%3A1211%2C%22pid%22%3A0%7D; MKT_OrderClick=ASID=4897155952&AID=4897&CSID=155952&OUID=index&CT=1670568669940&CURL=https%3A%2F%2Fwww.ctrip.com%2F%3Fsid%3D155952%26allianceid%3D4897%26ouid%3Dindex&VAL={}; __zpspc=9.80.1670572312.1670572325.3%232%7Cwww.baidu.com%7C%7C%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _jzqco=%7C%7C%7C%7C1670554470477%7C1.386356559.1667787833232.1670572320920.1670572325075.1670572320920.1670572325075.undefined.0.0.575.575; MKT_CKID=1667787833303.6cihj.yc0k; _RF1=171.109.34.146; _RSG=PI4tVah22dC4DYKmrdfaUA; _RDG=28a682bf6ceb192ebc37d846ca69b5ed63; _RGUID=c9c20ab9-1fdc-4499-a7a4-a67d70522344; MKT_Pagesource=PC; _bfaStatusPVSend=1; _bfaStatus=success; nfes_isSupportWebP=1; _ga=GA1.2.728287556.1667875987; Session=smartlinkcode=U130026&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; UUID=20EDDDB8AE46403495EFEE36FAC417C1; IsPersonalizedLogin=F; ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; ibu_h5_lang=en; ibu_h5_local=en-us; Hm_lvt_37b54c42b9dde393e60c88c1a84657cb=1668156071,1668390905,1668766327,1669630249; _lizard_LZ=ghjTSPinRlQVIkJmqrUWXFopstucvwx210a3ydz754YfM6ZE89+b-eKCHOLNBGAD; intl_ht1=h4=33_51616458,33_6550062,33_75424975,33_782288,2_441618; _abtest_userid=294c1513-b267-4324-8a01-750ac3d84f81; _gcl_au=1.1.920354234.1668409170; U_TICKET_SELECTED_DISTRICT_CITY=%7B%22value%22%3A%7B%22districtid%22%3A%222%22%2C%22districtname%22%3A%22%E4%B8%8A%E6%B5%B7%22%2C%22isOversea%22%3Anull%7D%2C%22createTime%22%3A1668416843913%2C%22updateDate%22%3A1668416843913%7D; FlightIntl=Search=[%22KWL|%E6%A1%82%E6%9E%97(KWL)|33|KWL|480%22%2C%22BJS|%E5%8C%97%E4%BA%AC(BJS)|1|BJS|480%22%2C%222022-11-17%22]; Hm_lvt_576acc2e13e286aa1847d8280cd967a5=1668916753; login_uid=C0AB45AFF50D550863B877680E735ABE; login_type=0; appFloatCnt=1; StartCity_Pkg=PkgStartCity=33; GUID=09031172114453342165; cticket=337E22BDC21DD4985842195D8CEDEC0C8B461417CA4C7D03098988464C0EFC5E; AHeadUserInfo=VipGrade=0&VipGradeName=%C6%D5%CD%A8%BB%E1%D4%B1&UserName=&NoReadMessageCount=0; DUID=u=C0AB45AFF50D550863B877680E735ABE&v=0; IsNonUser=F; Union=OUID=index&AllianceID=4897&SID=155952&SourceID=&createtime=1670568670&Expires=1671173469939; MKT_CKID_LMT=1670554468414; _bfi=p1%3D212094%26p2%3D212093%26v1%3D1210%26v2%3D1208; librauuid=; htltmp=; htlstmp=; _gid=GA1.2.1489218311.1670568674; _pd=%7B%22_o%22%3A3%2C%22s%22%3A272%2C%22_s%22%3A1%7D; _bfs=1.32; hotelhst=1164390341',

}

from datetime import date, timedelta
today = time.strftime("%Y-%m-%d", time.localtime())
tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")

from MysqlConnect import *
mysql = MysqlConnect()

# 爬取酒店的评论
class Xiecheng_Hotel:
    async def getComment(self,item, session, dic):
        try:
            data = json.loads(item['data'])
            async with session.post(item['url'], json=data) as res:
                resp = await res.json()
                # print(resp)
                totalCommentCount = 0
                dic['差评'] = 0
                dic['值得推荐'] = 0
                if resp['totalCount'] != None:
                    totalCommentCount = resp['totalCount']
                statisticList = resp['statisticList']
                travelTypeList = resp['travelTypeList']
                commentTagList = resp['commentTagList']
                othersComment = []
                # 评价标签
                for tag in travelTypeList:
                    tagName = tag['name']
                    tagcommentCount = tag['commentCount']
                    othersComment.append({f"{tagName}": tagcommentCount})
                # 评价标签
                for tag in commentTagList:
                    tagName = tag['name']
                    tagcommentCount = tag['commentCount']
                    othersComment.append({f"{tagName}": tagcommentCount})
                # 评价标签
                for tab in statisticList:
                    tabName = tab['name']
                    tabcommentCount = tab['commentCount']
                    if tabName == '值得推荐' or tabName == '差评' or tabName == '所有点评':
                        dic[f'{tabName}'] = tabcommentCount
                    else:
                        othersComment.append({f"{tabName}": tabcommentCount})
                dic['好评'] = dic['值得推荐'] - dic['差评']
                dic['中评'] = 0
                othersComment = str(othersComment)
                args = (
                item["id"], item["name"], totalCommentCount, dic['好评'], dic['中评'], dic['差评'], othersComment, today,
                "携程")
                print(args)
                sql = 'INSERT INTO hotel_comment(hotelId,hotelName,num,good,middle,bad,othersComment,crawlTime,siteFrom) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                mysql.insert(sql, args)
        except Exception as e:
            print('comment报错', e)
            time.sleep(5)
            await self.getComment(item,session,dic)

    # 从数据库获取酒店信息
    async def getHotel(self):
        async with aiohttp.ClientSession(headers=headers) as session:
            # 从数据库拿url
            results = mysql.queryHotel("select id,name,xc_url,xc_data from hotels where xc_url!='' and id > 1662 ", None)
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
                    "data": data
                })
            # print(list)
            print("携程网站的所有酒店长度", len(url_list))
            index = 0
            for item in url_list:
                index = index + 1
                dic = {"id": item['id'], "name": item['name'], 'flag': 0}
                item['url'] = "https://m.ctrip.com/restapi/soa2/24626/commentlist?_fxpcqlniredt=09031172114453342165&x-traceID=09031172114453342165-1670568709094-2810570"
                item['data'] = str(item['data']).replace(f'"pageIndex": 1,', f'"pageIndex": {index},')
                item['data'] = str(item['data']).replace(f'"pageIndex": {index - 1}', f'"pageIndex": {index}')
                task = asyncio.create_task(self.getComment(item.copy(), session, dic))
                if index % 8 == 0:
                    time.sleep(5)
                tasks.append(task)
                await asyncio.wait(tasks)
            print("爬完了！！！！")
            # 关闭mysql
            mysql.cur.close()
            mysql.connection.close()


if __name__ == '__main__':
    # saveHotel()
    asyncio.run(getHotel())
