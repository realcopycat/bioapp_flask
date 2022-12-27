import requests
import re
import aiohttp
import asyncio
import csv
import json
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
}

from datetime import date, timedelta
today = time.strftime("%Y-%m-%d",time.localtime())
tomorrow = (date.today() + timedelta(days= 1)).strftime("%Y-%m-%d")

from MysqlConnect import *
mysql = MysqlConnect()


class Xiecheng_Scenic:
    # 爬取景区基本信息
    def getBaseInfo(self,html):
        # 初始化搜索条件
        dic = {}
        obj = re.compile(r'<h1>(?P<name>.*?)</h1>.*?'
                         r'titleTips"><span>(?P<level>.*?)</span>.*?'
                         r'commentScoreNum">(?P<score>.*?)</p>.*?'
                         r'hover-underline">(?P<commentNum>.*?)<!-- -->.*?'
                         # r'地址</p><p class="baseInfoText">(?P<address>.*?)</p>.*?'
                         r'开放时间</div><div class="moduleContent">(?P<time>.*?)</div>.*?'
                         r',"poiId":(?P<poiId>.*?),"poiType"'
                         r'', re.S)
        # 有些景点没有等级 的处理方法
        tempobj1 = re.compile(r'titleTips"><span>(?P<level>.*?)</span>.*?', re.S)
        tempres1 = tempobj1.search(html)
        if tempres1 == None:
            dic['level'] = 0
            obj = re.compile(r'<h1>(?P<name>.*?)</h1>.*?'
                             r'commentScoreNum">(?P<score>.*?)</p>.*?'
                             r'hover-underline">(?P<commentNum>.*?)<!-- -->.*?'
                             # r'地址</p><p class="baseInfoText">(?P<address>.*?)</p>.*?'
                             r'开放时间</div><div class="moduleContent">(?P<time>.*?)</div>.*?'
                             r',"poiId":(?P<poiId>.*?),"poiType"', re.S)
        else:
            dic['level'] = tempres1.group('level')
        # 有些景点没有评分
        tempobj2 = re.compile(r'commentScoreNum">(?P<score>.*?)</p>.*?'
                              r'hover-underline">(?P<commentNum>.*?)<!-- -->.*?'
                              , re.S)
        tempres2 = tempobj2.search(html)
        if tempres2 == None:
            dic['score'] = 0
            obj = re.compile(r'<h1>(?P<name>.*?)</h1>.*?'
                             # r'地址</p><p class="baseInfoText">(?P<address>.*?)</p>.*?'
                             r'开放时间</div><div class="moduleContent">(?P<time>.*?)</div>.*?'
                             r',"poiId":(?P<poiId>.*?),"poiType"', re.S)
            # 有些景点没有评分
        else:
            dic['score'] = tempres2.group('score')
        tempobj3 = re.compile(r'hover-underline">(?P<commentNum>.*?)<!-- -->.*?'
                              , re.S)
        tempobj3 = tempobj3.search(html)
        if tempobj3 == None:
            dic['commentNum'] = 0
            return dic
        else:
            dic['commentNum'] = tempobj3.group('commentNum')
        # 最终爬取景点基本信息并存入
        resp1 = obj.search(html)
        # print(resp1.group('name') + '爬取成功')
        if resp1 != None :
            dic = resp1.groupdict()
        if tempres1 != None:
            dic['level'] = dic['level'].replace('<!-- -->', '')
        return dic

    # 爬取评论标题
    def getCommentTitle(self,html, dic,othersComment):
        obj = re.compile(r'"hotTag">(?P<title>.*?)</span>.*?', re.S)
        titles = obj.finditer(html)
        i = 0
        for item in titles:
            good = item.group('title').split('<!-- -->')
            good[1] = good[1].replace('(', '').replace(')', '')
            # print(good)
            if good[0] == '好评' or good[0] == '差评':
                dic[f'{good[0]}'] = good[1]
            else:
                othersComment.append({f"{good[0]}": good[1]})
            i = i + 1

    # 爬取网页具体信息ok
    async def getDetail(self,item, session):
        tasks = []
        try:
            async with session.get(item['url']) as res:
                html = await res.text()
                dic = self.getBaseInfo(html)
                othersComment = []
                dic["好评"] = 0
                dic["中评"] = 0
                dic["差评"] = 0
                self.getCommentTitle(html, dic, othersComment)
                othersComment = str(othersComment)
                args = (item["id"], item["name"], dic["score"], dic["commentNum"], dic["好评"], dic["中评"], dic["差评"], othersComment,
                today,"携程")
                print(args)
                sql = f'INSERT INTO scenic_comment(scenicId,scenicName,score,num,good,middle,bad,othersComment,crawlTime,siteFrom) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                mysql.insert(sql, args)
        except Exception as e:
            print("comment报错",e)
            time.sleep(5)
            await getDetail(item,session)


    async def getScenic(self):
        async with aiohttp.ClientSession(headers=headers) as session:
            results = mysql.query("select id,name,xc_url from scenics where xc_url !=''", None)
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
            tasks = []
            print("携程网站的所有景区长度", len(url_list))
            i = 0
            for item in url_list:
                task = asyncio.create_task(self.getDetail(item, session))
                i = i + 1
                tasks.append(task)
                if i % 5 == 0 :
                    time.sleep(5)
                await asyncio.wait(tasks)
            # 关闭mysql
            mysql.cur.close()
            mysql.connection.close()

if __name__ == '__main__':
    asyncio.run(getScenic())