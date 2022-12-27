import requests
import re
import aiohttp
import asyncio
import csv
import json
import os
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
}
from datetime import date, timedelta
today = time.strftime("%Y-%m-%d",time.localtime())
tomorrow = (date.today() + timedelta(days= 1)).strftime("%Y-%m-%d")

from MysqlConnect import *
mysql = MysqlConnect()

# 爬取一个景区的评论
class Tongcheng_Scenic:
    async def getComment(self,item, pageIndex, session, dic):
        try:
            async with session.post(item['url']) as res:
                res1 = await res.text()
                res1 = json.loads(res1)
                if pageIndex == 1:
                    dic['degreeLevel'] = res1['degreeLevel']
                    dic['totalNum'] = res1['totalNum']
                    dic['goodNum'] = res1['goodNum']
                    dic['midNum'] = res1['midNum']
                    dic['badNum'] = res1['badNum']
                    dic['hasImgNum'] = res1['hasImgNum']
                    dpTagList = res1['dpTagList']
                    othersComment = []
                    i = 0
                    if dpTagList != None:
                        for dpTag in dpTagList:
                            if i > 5 :
                                othersComment.append({f"{dpTag['tagName']}":dpTag['tagNum']})
                            i = i + 1
                    othersComment = str(othersComment)
                    args = (item["id"], item["name"], dic["degreeLevel"], dic["totalNum"], dic['goodNum'], dic['midNum'], dic['badNum'], othersComment,today, "同程")
                    print(args)
                    sql = 'INSERT INTO scenic_comment(scenicId,scenicName,satisfy_present,num,good,middle,bad,othersComment,crawlTime,siteFrom) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                    mysql.insert(sql, args)
        except Exception as e:
            print(e)

    async def getScenic(self):
        async with aiohttp.ClientSession(headers=headers) as session:
            results = mysql.query("select id,name,tc_url from scenics where tc_url !='' ", None)
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
            print("同程网站的所有景区长度", len(url_list))
            i = 0
            for item in url_list:
                dic = {}
                task = asyncio.create_task(self.getComment(item, 1, session, dic))
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

