#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：爬虫 -> test
@IDE    ：PyCharm
@Author ：sandmswift
@Date   ：2022-11-17 16:21
@Desc
=================================================='''
import happybase

con = happybase.Connection("202.193.53.106")
con.open()

con.create_table("tuniu_scenic",{
    'info':dict(),
    'comments':dict(),
})
con.create_table("scenic_hotel",{
    'info':dict()
})
con.create_table("weibo",{
    'info':dict()
})
con.create_table("tongchen",{
    'info':dict()
})
con.create_table("bauduacc",{
    'info':dict(),
    'all':dict(),
    'wise':dict()
})
con.create_table("baiduwords",{
    'info':dict()

})
con.create_table("baudusearch", {
    'info': dict()

})

con.close()