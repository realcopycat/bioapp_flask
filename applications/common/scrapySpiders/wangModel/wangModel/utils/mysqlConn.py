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

def get_conn():
    conn = pymysql.connect(host='202.193.53.151', port=3306, user='root', passwd='root', db='travel')
    return conn

"""
查询数据库
"""
def getRows(sql,args):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql, args)
    results = cur.fetchall()
    return results

def query(sql,args):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql,args)
    results = cur.fetchall()
    # print(type(results))  # 返回<class 'tuple'> tuple元组类型
    list=[]
    for row in results:
        id=row[0]
        name=row[1]
        url=row[2]
        list.append({
            "id":id,
            "name":name,
            "url":url
        })
    print(list)
    conn.commit()
    cur.close()
    conn.close()
    return list

"""
插入数据库
"""
def insert(sql, args):
    conn = get_conn()
    cur = conn.cursor()
    result = cur.execute(sql, args)
    # print(result)
    conn.commit()
    cur.close()
    conn.close()

"""更新"""
def update(sql,args):
    conn = get_conn()
    cur = conn.cursor()
    result = cur.execute(sql,args)
    print(result)
    conn.commit()
    cur.close()
    conn.close()


# if __name__ == '__main__':
#     sql="select id,name,tn_url from scenics where tn_url !='' "
#
#     query(sql,None)
    # sql = 'INSERT INTO scenic_comment(scenicId,scenicName,satisfy_present,num,good,middle,bad) VALUES(%s,%s,%s,%s,%s,%s,%s);'
    # insert(sql, (2, 'wang', 13))
