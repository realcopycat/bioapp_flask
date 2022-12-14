#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：爬虫 -> connTest
@IDE    ：PyCharm
@Author ：sandmswift
@Date   ：2022-11-11 11:31
@Desc
=================================================='''
import happybase
# con=happybase.Connection(host=’localhost’, port=9090, timeout=None, autoconnect=True, table_prefix=None, table_prefix_separator=b’_’, compat=’0.98’, transport=’buffered’, protocol=’binary’)
# 不配置参数的话直接简单连接 thrift的默认端口就是9090

class HbaseUtil:
    def __init__(self,con):
        self.con=con
        self.con = happybase.Connection(con)
        self.con.open()
    """
    插入数据
    参数：表名，行键，数据：键值对
    数据实例：左边是列族：列名，右边是插入的数据
    data= { "info:name": "lisa",
            "info:address":"Beijing" 
            }
    """
    def putTable(self,tablename,rowkey,data):
        table=self.con.table(tablename)
        table.put(rowkey,data)
        # self.con.close()

    def batchTable(self,tablename,rowkey,data):
        table=self.con.table(tablename)
        bat=table.batch()
        bat.put(rowkey,data)
        bat.send()
        # self.con.close()

    """
    获取所有表名
    """
    def getTables(self):
        print(self.con.tables())

    def closeCon(self):
        self.con.close()


# #
# obj=HbaseUtil('202.193.53.106') #连接
# obj.getTables() #查看表
# """


