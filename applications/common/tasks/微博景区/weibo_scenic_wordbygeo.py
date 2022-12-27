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
    'Cookie':"SINAGLOBAL=6487030870592.412.1670217755062; ULV=1670913619949:2:2:1:448084127526.90094.1670913619909:1670217755065; SUB=_2A25OnG8QDeRhGeFG61oQ9CfOyzWIHXVt6MfYrDV8PUNbmtANLXbRkW9NfnN7XS0bIXvPWvBx4AplvHeMTR0yYZWh; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhuyxuyZV28mO7UcSyqZia-5JpX5KzhUgL.FoMRehnpSh.Eeh.2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoM71K201h27eKBc; XSRF-TOKEN=Nb98b84zpKrLkQFK2G4QVm_B; WBPSESS=GXgdHCdzDjVRXBTFCQtCjwvN0D3EIjJu6yKjC9Ly2vpYlmMNPvd-am2fVfhb0LZzGlpu1z5hvjfehJnVFqrpORnpezcjqLRXjHTwRYkqud2f-lo5ogx3FJhjiiEoA2AHWwC4_I4Ebc8XETWMRRXqRQ==; _s_tentry=-; Apache=448084127526.90094.1670913619909; appkey=; ALF=1702449855; SSOLoginState=1670913856",
    # 'referer': 'https://s.weibo.com/'
}

from MysqlConnect import *
mysql = MysqlConnect()

class Weibo_Wordbygeo:
    async def getWord(self,item, session):
        try:
            maxPage = int(item['maxPage'])
            wordList = []
            for index in range(1,maxPage+1):
                url = f"https://s.weibo.com/weibo?q={item['short_name']}&page={index}"
                async with session.get(url) as res:
                    res = await res.text()
                    tempList = re.compile(r'>#(.*?)#<').findall(res)
                    wordList.extend(tempList)
                if index % 8 == 0:
                    print(f"<----------------{item['short_name']}爬到{index}页------------------->")
                    time.sleep(3)
            # 微博fans的sql
            args = (item["id"], item["short_name"], str(wordList), today)
            print(args)
            sql = 'INSERT INTO weibo_word(scenicId,name,wordList,crawlTime) VALUES(%s,%s,%s,%s);'
            mysql.insert(sql, args)
        except Exception as e:
            print("fans报错",e)

    # 从数据库获取景区信息
    async def getScenic(self):
        async with aiohttp.ClientSession(headers=headers) as session:
            # 从数据库拿url
            results = mysql.queryHotel("select id,name ,short_name from scenics where id > 0", None)
            tasks = []
            url_list = []
            for row in results:
                id = row[0]
                name = row[1]
                short_name = row[2]
                url_list.append({
                    "id": id,
                    "name": name,
                    "short_name": short_name,
                })
            print("微博所有景区长度", len(url_list))
            for item in url_list:
                url = f"https://s.weibo.com/weibo?q={item['short_name']}&page=1"
                res = requests.get(url, headers=headers)
                maxPages = re.compile(r'第(.*)页').findall(res.text)
                if maxPages == []:
                    item['maxPage'] = 1
                else:
                    item['maxPage'] = maxPages[len(maxPages) - 1]
                print(item['short_name'] + f'长度为：{item["maxPage"]}')
                task = asyncio.create_task(self.getWord(item.copy(), session))
                tasks.append(task)
                await asyncio.wait(tasks)
                print(f"{item['short_name']}爬完了")
            # 关闭mysql
            mysql.cur.close()
            mysql.connection.close()

if __name__ == '__main__':
    asyncio.run(getScenic())
