#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：爬虫 -> weibosign
@IDE    ：PyCharm
@Author ：sandmswift
@Date   ：2022-11-23 17:56
@Desc
=================================================='''
import random
import time
from time import mktime
import datetime
import requests
from wangModel.utils.proxys import ips
import requests
from bs4 import BeautifulSoup
import json
import re
import time
import sqlite3, pandas
import random
import traceback
import threading
from snownlp import SnowNLP
from wangModel.utils.mysqlConn import insert, query, getRows
from snownlp import SnowNLP


class WeiboSignSpider():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56",
        "MWeibo-Pwa": "1",
        "X-XSRF-TOKEN": "02df4d",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": "SUB=_2A25OhDMBDeRhGeBP7lMU-SbKyT6IHXVth11JrDV6PUJbktANLRWkkW1NRVCnaEGA4AX519XF_MMcAtaGMSsUMm8O; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5zvTRN3-zLYaqhYgDN-85m5NHD95QceK-pSK.RSozEWs4Dqc_zi--Xi-zRiKy2i--NiKnRi-zpi--Ri-8si-zXi--Ri-8siKL2i--NiKLWiKnXi--4iK.Ri-z0i--fiK.0i-2fi--fiK.0i-2f; SSOLoginState=1669350225; _T_WM=83963246267; WEIBOCN_FROM=1110006030; MLOGIN=1; __bid_n=184ad2413b313dd7364207; FPTOKEN=30$YVRFaVAuo0Hb+ZCeGddk5p5th37hiAH3OD/a7GIZ/EifG6bPi/j090zR3KK9++fg6peU2CIuZsSJWb/gQj1NoDsjbDRvlOefETnNuv4Zx11df54uM5cp7GO2lRldfLaA/H0Y1zFlg/Et1NrarB+/IC8nPG9aAU2D70bJMXbH2aik3ZAMz6ybL1NhYR6i9lr5t0C1gGbRj585QemHLaRPPW+34QZApuuOhdJhI5rUu0OeCbHkoapziul6hHk+JUco1CFHGxiBnJPluvUa+VmnTGOUBxaur7ndbiECeY9AZOyh/cY2gfnBjO37BqXekHdwimFEqIpYaTUFDpMmOCS/DnRhY6nfcZ4xLtQclnzUHMZiywGLlV0rmzQujNPb6EgK|5ByMysyxg5uNsuQAFYoC08fks57jzZCDUASGWGvQH9U=|10|60e86591f8b07231e25ee3e8ee7a1014; XSRF-TOKEN=02df4d; mweibo_short_token=cf30a892e2; BAIDU_SSP_lcr=https://cn.bing.com/; M_WEIBOCN_PARAMS=oid%3D4839655495435847%26luicode%3D20000061%26lfid%3D4839655495435847%26uicode%3D20000061%26fid%3D4839655495435847"
    }

    lasterTime = ""
    flag=0

    # 爬虫基本功能部分，返回网页的一个json
    def get_tweets(self, URL, page, ippool):
        url = URL.format(str(page))
        while True:
            try:
                proxy_ip = "http://" + random.choice(ips)
                time.sleep(3)
                res = requests.get(url, headers=self.header)
                res.encoding = 'utf-8'
                soup = BeautifulSoup(res.text, 'html.parser')
                jd = json.loads(res.text)
                # print(jd)

            except:
                print('代理有问题呀，换个ip试试')
                continue

            if (jd['ok'] == 0) and ("这里还没有内容" in str(jd)):
                print(jd)
                return 0

            if jd['ok'] == 0:
                print('获取地点的页面失败啊，换个ip试试')
            else:
                break

        # 第一页的结果会有点不一样
        if page == 1:
            if 'card_id' in jd['data']['cards'][0]:
                if jd['data']['cards'][0]['card_id'] == 'card_hq_poiweibo':
                    tweets = jd['data']['cards'][0]['card_group']
                    return tweets
                else:
                    tweets = jd['data']['cards'][1]['card_group']
                    return tweets
        else:
            card_id=jd['data']['cards'][0]['card_id']
            if(card_id!="hot_search"):
                tweets = jd['data']['cards'][1]['card_group']
            else:
                tweets = jd['data']['cards'][0]['card_group']

        # print(tweets)
            return tweets

    def writedb(self, items, page):
        # 遍历每条微博
        if items:
            print("评论长度",len(items))
            for i in range(len(items)):
                print("内容",items[i])
                # 整理微博表的数据
                temp = [0 for i in range(13)]  # 初始化一行，一共有11列
                # print(temp)
                if 'mblog' in items[i]:
                    temp[0] = items[i]['mblog']['id']
                    if "id" in items[i]['mblog'] and temp[0] is  not  None:
                        temp[1] = current_time
                        temp[2] = items[i]['mblog']['created_at']
                        temp[3] = items[i]['mblog']['user']['id']
                        temp[4] = items[i]['mblog']['source']
                        temp[5] = re.sub("[A-Za-z0-9\!\%\[\]\,\。\<\-\=\"\:\/\.\?\&\_\>\'\;\ ]", "", items[i]['mblog']['text'])
                        s2 = SnowNLP(temp[5])
                        # print(temp[5], s2.sentiments)
                        temp[6] = items[i]['mblog']['reposts_count']
                        temp[7] = items[i]['mblog']['comments_count']
                        temp[8] = items[i]['mblog']['attitudes_count']
                        temp[9] = items[i]['mblog']['pending_approval_count']
                        temp[10] = place
                        temp[11] = scenicId

                        # 删掉来源里面那些乱七八糟的字符
                        temp[4] = temp[4].replace("'", "")
                        temp[4] = temp[4].replace('"', '')
                        temp[5] = str(temp[5]).replace("#", "").replace("🌸", "")
                        # print("品论内容",type(temp[5]))

                        s = time.strptime(temp[2], '%a %b %d %H:%M:%S +0800 %Y')
                        remarkTime = str(s.tm_year) + "-" + str(s.tm_mon) + "-" + str(s.tm_mday) + " " + str(
                            s.tm_hour) + ":" + str(
                            s.tm_min) + ":" + str(s.tm_sec)
                        remarkTime = time.strptime(remarkTime, '%Y-%m-%d %H:%M:%S')
                        remarkTime=datetime.datetime(*remarkTime[:6])
                        # print("该景区最新评论时间是",remarkTime)

                        flag = 0
                        args = (temp[11], temp[10], temp[3], temp[4], str(temp[5]), temp[6], temp[7], temp[8], remarkTime,
                                datetime.date.today())
                        if self.lasterTime is None:
                            # 写入数据库
                            sql = "insert into weibosign(scenicId,scenicName,user_id,sourcefrom,content,reports_count,comments_count,attitudes_count,sign_time,crawlTime) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                            insert(sql, args)
                            print("插入数据",temp)
                            print('Page', page, ' %s 这条微博写进微博表啦' % temp[0])
                            flag = 1
                            self.flag=flag
                        # return flag
                        elif  self.lasterTime < remarkTime:
                            # 写入数据库
                            sql = "insert into weibosign(scenicId,scenicName,user_id,sourcefrom,content,reports_count,comments_count,attitudes_count,sign_time,crawlTime) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                            insert(sql, args)
                            print('Page', page, ' %s 这条微博写进微博表啦' % temp[0])
                            flag = 1
                            self.flag = flag
                        else:
                            flag=0
                            self.flag = flag


                else:
                    pass

    # 爬取指定景点的微博数据
    def main(self, row, ippool):

        global conn, cur, place, pid, scenicId
        scenic = getRows("select name,wb_scenicId,id from scenics where wb_scenicId!=''", None)
        # 读取资料文档
        # place = scenic[row][0]
        # pid = scenic[row][1]
        # scenicId = scenic[row][2]
        place = scenic[row+1][0]
        pid = scenic[row+1][1]
        scenicId = scenic[row+1][2]
        print("景点名称：%s,景点id:%s,景点网站id:%s" % (place, scenicId, pid))

        # 判断微博第一条是否已经爬过
        selectHasTimeSql = "select sign_time from weibosign where scenicId=%s order by sign_time desc"
        databaseComment = getRows(selectHasTimeSql, scenicId)
        print("查询数据库景点评论数据时间列表", databaseComment)
        # 获取上一次爬取的最新评论时间
        lasterDate = None
        if databaseComment:
            # 格式转化
            lasterDate = databaseComment[0][0]
            print("最新时间是", lasterDate)

        self.lasterTime = lasterDate

        print('******************开始爬%s的微博了*******************************' % place)
        try:
            time_start = time.time()

            # 爬150页微博
            # page = 1
            for page in range(1, 150):
                # 微博位置URL
                URL = 'https://m.weibo.cn/api/container/getIndex?containerid=' + pid + f'&luicode=10000011&lfid=100103type%3D1%26q%3D%E6%AD%A6%E6%B1%89%E5%A4%A7%E5%AD%A6&page={page}'
                print('开始爬', place, '第', page, '页')

                # 获取当前时间
                global current_time
                current_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
                # 获取一个页面的所有内容，json格式
                tweets = self.get_tweets(URL, page, ippool)

                # 判断是不是到底了
                if "周边值得去" in str(tweets):
                    print('爬到底了！')
                    break

                if tweets == 0:
                    print('已经到第', page, '页了，没有内容了')
                    break

                self.writedb(tweets,page)
                flag = self.flag
                print("爬取结果的标志", flag)
                if flag==0:
                    print("该景点最新的数据已经存完啦")
                    break
                else:
                    print(place, ' 第', page, '页爬完了！')
                    page += 1
                    continue

            time_end = time.time()
            print(place, ' time cost ', time_end - time_start, 's')

            print('******************%s的微博爬完了*******************************' % place)


        except:
            e = traceback.format_exc()
            # 要是报错了，就发邮件然后退出
            print(e)

        print(place, '爬完了！等待下一次')

    def run(self):
        rows = getRows("select count(*) from scenics where wb_scenicId!=''", None)
        n = rows[0][0]
        for i in range(n):
            self.main(i, ips)
# if __name__ == '__main__':
#     web = WeiboSignSpider()
#     web.run()
