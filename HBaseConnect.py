# -*- coding: utf-8 -*-
import happybase
import json
import re


# 实现连接类方法和通用表操作方法
class HBaseConnect:
    def __init__(self):
        """
        建立与thrift server端的连接
        """
        self.connection = happybase.Connection(host="202.193.53.106", port=9090, timeout=None, autoconnect=True,
                                               table_prefix=None, table_prefix_separator=b'_', compat='0.98',
                                               transport='buffered', protocol='binary')

    def getTable(self, table_name: str):  # Return Happybase Table
        return self.connection.table(table_name)

    def start(self):  # Start To Connect
        self.connection.open()

    def stop(self):  # Stop To Connect
        self.connection.close()

    # 删除表
    def deleteTable(self, tableName):
        self.connection.disable_table(tableName)
        self.connection.delete_table(tableName)

    def printTables(self):
        return self.connection.tables()

    def createTable(self, tableName, families):
        self.connection.create_table(tableName, families)

    def putTable(self, tableName, rowKey, data):
        table = self.connection.table(tableName)
        table.put(rowKey, data)


if __name__ == '__main__':
    hbase = HBaseConnect()
    hbase.start()
    # hbase.deleteTable("qunaerscenic")
    # list = ["xiechenghotel","xiechengscenic","qunaerhotel","qunaerscenic","tongchenghotel","tongchengscenic",]
    # for item in list:
    #     #
    #     # hbase.deleteTable(item)
    #     hbase.createTable(item, {"info": dict()})
        #
    # hbase.putTable("xiechenghotel","test",{"info:name":"23"})
    # hbase.deleteTable("tongchengscenic")
    # hbase.createTable('route_comment', {"info": dict()})
    table = hbase.getTable("route_comment")
    i=0
    # id = 3909
    for key, value in table.scan():
        data = str(value).encode().decode('unicode-escape').encode('raw_unicode_escape').decode()
        # print(len(data))
        # i=i+1
        # res = re.compile(rf"b'info:datafrom': b'去哪儿', b'info:hid': b'1853'").search(data)
        # if res != None:
        #     i=i+1
        #     # table.delete(key)
        #     print(data)
        res = re.compile(r"info:content': b'用户未及时评价, 该评价为系统默认好评!'").search(data)
        if res != None:
            i=i+1
            print(data)
            table.delete(key)
        res = re.compile(r"info:content': b'用户未填写文字评价。").search(data)
        if res != None:
            i=i+1
            print(data)
            table.delete(key)
        # print (str(data))
    print(i)
    # print(hbase.printTables())
    hbase.stop()

"""
data={
        'info:place_from': item['place_from'],
        'info:place_to': item['place_to'],
        'info:Date': item['Date'],
        'info:totalCount': item['totalCount'],
        'info:type': item['type'],
        'info:ticketStatus': item['ticketStatus']
            }
    obj.putTable("表名","行键",data)   #插入语句
"""
