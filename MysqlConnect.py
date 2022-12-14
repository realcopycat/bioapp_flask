#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：爬虫 -> mysqlConn
@IDE    ：PyCharm
@Author ：sandmswift
@Date   ：2022-11-21 10:54
@Desc
=================================================='''
import pymysql


# 实现连接类方法和通用表操作方法
class MysqlConnect:
    # 初始化数据库
    def __init__(self):
        print()
        self.connection = pymysql.connect(host='202.193.53.151', port=3306, user='root', passwd='root', db='travel',charset='utf8mb4')
        self.cur = self.connection.cursor()

    def query(self,sql, args):
        self.cur.execute(sql, args)
        results = self.cur.fetchall()
        # print(type(results))  # 返回<class 'tuple'> tuple元组类型
        # self.connection.commit()
        return results

    def queryHotel(self,sql, args):
        self.cur.execute(sql, args)
        results = self.cur.fetchall()
        # print(type(results))  # 返回<class 'tuple'> tuple元组类型
        self.connection.commit()
        return results

    def update(self,sql,args):
        # 携程修改的sql
        self.cur.execute(sql,args)
        self.connection.commit()

    # 封装插入数据到数据库
    def insert(self,sql, args):
        # 携程和去哪儿景区
        # sql = f'INSERT INTO {tableName}(scenicId,scenicName,score,num,good,middle,bad,othersComment,crawlTime,siteFrom) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        # 同程景区
        # sql = 'INSERT INTO scenic_comment(scenicId,scenicName,satisfy_present,num,good,middle,bad,othersComment,crawlTime,siteFrom) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'

        # 同程酒店内容
        # sql = f'INSERT INTO hotels(name,level,address,tc_url,tc_data,crawlTime) VALUES(%s,%s,%s,%s,%s,%s);'
        # 同程和去哪儿酒店
        # sql = 'INSERT INTO hotel_comment(hotelId,hotelName,num,good,middle,bad,othersComment,crawlTime,siteFrom) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);'

        result = self.cur.execute(sql, args)
        # print(result)
        self.connection.commit()

# if __name__ == '__main__':
#     mysql = MysqlConnect()
#     mysql.update((222,"诗与远方·漓江院子酒店(两江四湖东西巷店)"))