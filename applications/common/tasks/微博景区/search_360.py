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
    'Host': 'trends.so.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://trends.so.com/result?query=%E6%BC%93%E6%B1%9F,%E8%B1%A1%E5%B1%B1&period=30',
    'Cookie': '__guid=239254294.3977692736380259300.1670144255177.8064; __gid=239254294.318323770.1670144255178.1670144261083.38; __bn=OBOS%7BOxOnSwO%24O%2FBVKQFw%3CS%3EStwRt3BqwL%2C%2B%2FUpx.pdL%28UoxX%294STo1Dzg%2F%7DVYG%40dJp%3F1M%40f%5EJ0%7Cs%3ClLe%5E%23OAT8gZKW%232LE%7C9ue%25YHrkL_c8y%2AnNf5v%26LmJ7%5Eh%21_6; QiHooGUID=4B479C909060D45303A26176A83571EE.1670921647212; count=2; test_cookie_enable=null; Q=u%3D360H3408265314%26n%3D%25Q3%25Q0%25Q0%25P4%25P8%25PO_308%26le%3D%26m%3DZGH1WGWOWGWOWGWOWGWOWGWOBQt0%26qid%3D3408265314%26im%3D1_t015d6b97def2a4a918%26src%3Dpcw_360index%26t%3D1; T=s%3D6b400eed78c7fa7b27a496343be40f86%26t%3D1670921768%26lm%3D0-1%26lf%3D2%26sk%3Dc5c99806e7fcea7539ea20e35943912a%26mt%3D1670921768%26rc%3D%26v%3D2.0%26a%3D1; so_huid=11k1XvfU5zrG3%2BT9U%2FzH9XHKHrh6tHE07PUntGARvW36A%3D; __huid=11k1XvfU5zrG3%2BT9U%2FzH9XHKHrh6tHE07PUntGARvW36A%3D; _S=fd41ea22d44de0791f9996eaa25d084e',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers',
}

from MysqlConnect import *
mysql = MysqlConnect()

class Search_360:
    async def getFans(self,item, session):
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
                task = asyncio.create_task(self.getFans(item.copy(), session))
                tasks.append(task)
                await asyncio.wait(tasks)
                print(f"{item['short_name']}爬完了")
            # 关闭mysql
            mysql.cur.close()
            mysql.connection.close()
    def test():
        url = "https://trends.so.com/index/soMediaJson?q=漓江,象山&from=20130111&to=20221212&s=0"
        res = requests.post(url,headers=headers)
        # print(res.json())
        resp = res.json()
        data = resp['data']['media']['漓江']
        # resp = res.content.decode('unicode-escape', 'ignore').encode('utf-8', 'ignore').decode('utf-8')  # 爬取页面并且解码
        print(data)

if __name__ == '__main__':
    test()
    # asyncio.run(getScenic())
