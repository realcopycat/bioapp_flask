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

# year = time.strftime("%Y-", time.localtime())
today = time.strftime("%Y-%m-%d",time.localtime())
tomorrow = (date.today() + timedelta(days= 1)).strftime("%Y-%m-%d")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    # 'Cookie':"SINAGLOBAL=3380569287618.6953.1670308366047; _s_tentry=s.weibo.com; Apache=5236619054300.727.1670324406000; ULV=1670324406003:2:2:2:5236619054300.727.1670324406000:1670308366049; XSRF-TOKEN=13toiK7TaB8Axa4Vx7DncNNO; login_sid_t=ec7d5e0d423e9ec19b8acb14ea31e88f; cross_origin_proto=SSL; wb_view_log=2560*14401.5; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCcqTynPQA63zJA5y17Xs15JpX5o275NHD95QcSoe0eo5XSo-fWs4Dqc_xi--fiK.0i-8Wi--ciKLhiKn4i--4iKnEi-20i--Xi-z4iKnRi--fi-2XiKLWi--ci-zpiKnEi--RiKn7iKyhi--Xi-zRiKy2i--fi-i8iK.N; SSOLoginState=1670812852; SUB=_2A25OkuTlDeRhGeBI6FET8CrKzjmIHXVt5lEtrDV8PUNbmtANLWiskW9NRptelGTTlu3DzUc2k9u71P0K706eTg71; ALF=1702348852; WBPSESS=QRnN_8uUPIRKDidMZ7ysnFsKmswTd-coyxvC3kx2wmVsnZYfCgM3CVbyYUESYHrYB0_OPXwWvhlacPaYtSVNXY0EckXCBF-9xxe7fsm2CcjhwFzQ2yBIcsDsTtMkf5Epp7PzpdyQGn9mf7C9CvIb3w==",
    # 'referer': 'https://s.weibo.com/'
}

from MysqlConnect import *
mysql = MysqlConnect()

class Weibo_Trend:
    async def getTalk(self,item, session):
        try:
            url = f"https://m.s.weibo.com/ajax_topic/detail?q={item['short_name']}"
            async with session.get(url) as res:
                resp = await res.json()
                read = 0
                ori_uv = 0
                mention = 0
                star = 0
                if 'count' in resp['data']['baseInfo']:
                    read = resp['data']['baseInfo']['count']['read']
                    ori_uv = resp['data']['baseInfo']['count']['ori_uv']
                    mention = resp['data']['baseInfo']['count']['mention']
                    star = resp['data']['baseInfo']['count']['star']
                args = (item["id"], item["short_name"], read,ori_uv,mention,star, today)
                print(args)
                sql = 'INSERT INTO weibo_trend(scenicId,`name`,`read`,ori_uv,mention,star,crawlTime) VALUES(%s,%s,%s,%s,%s,%s,%s);'
                mysql.insert(sql, args)
        except Exception as e:
            print("fans报错",e)

    # 从数据库获取景区信息
    async def getScenic(self):
        async with aiohttp.ClientSession(headers=headers) as session:
            # 从数据库拿url
            results = mysql.queryHotel("select id,name ,short_name from scenics where id > 0 ", None)
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
            i = 0
            for item in url_list:
                task = asyncio.create_task(self.getTalk(item.copy(), session))
                tasks.append(task)
                i = i + 1
                if i % 8 == 0:
                    time.sleep(3)
                await asyncio.wait(tasks)
            # 关闭mysql
            mysql.cur.close()
            mysql.connection.close()
if __name__ == '__main__':
    asyncio.run(getScenic())