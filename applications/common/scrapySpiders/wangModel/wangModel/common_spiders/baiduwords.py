#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：爬虫 -> baiduwords
@IDE    ：PyCharm
@Author ：sandmswift
@Date   ：2022-11-16 10:21
@Desc:百度百科搜索词条
=================================================='''
from urllib import parse
import time
import random
import re
import requests
from wangModel.utils.proxys import PROXY,ips
from lxml import etree
import datetime
from wangModel.utils.mysqlConn import query,insert,getRows,update
from selenium import webdriver
class BaiDuWords():

    def parse(self,id,kw):
       url=f"https://baike.baidu.com/item/{parse.quote(kw)}?fromtitle={parse.quote(kw)}"
       print(url)
       header = {
            "X-Requested-With":"XMLHttpRequest",
           "Cipher-Text": "1668409355251_1668493173103_aLgQH4YFqAwPcYSE7v52xdJaHSAeId9tI+WY1JMiHu8HwngWY2DifDL8GwYz2O+DvIVgj+9ldrUsKJ3ADGdnEUHL1GARwcCChi73BbkUFeNFtACrNrwhmPStsz0iWKZEK1aqGImhb+zMQg9/qJkxFRR+4AuJz5zbU+IkH793cccuV18DONXlam0zLfF07BZFrBRtTFCC7P7YOpfz9du1sz0OHMxRr7Iwdq1hrNzZ0yW4pzm8Hw2C7gvEfXs81XQSHDeGOtaoZ/IQyn5QqCYSsGC47kiKIeEy2hOaGITVWj4wBHvNe//u+dxPX/cDPjIM7QWoQnmSAg2qOAUtzTMnBE0Eal21o3C03eGBGNJHXYM9xVQz2OEs+NeMG2HXjKi5boG4R8ypMvU8D5JsL9lU7G2WStNDiX7sEjaskomtx2g=",
           "Referer": "https://baike.baidu.com/item/%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91?fromModule=lemma_search-box",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52",
           "Cookie": "BIDUPSID=B772A7AE03D22C237EA5162D657EFEA8; PSTM=1646828464; BAIDUID=EF08EE41A5B9911A97D741FCA1E975AB:FG=1; FPTOKEN=30$MrCecZxUi8VS8olQk6GALxBMkPjNDvPqJaUEnW0U/il23iuvfUkXY4mgGNIFtYpKGevoBroMxF6rVAASyZuGaOxurO6Vofyd98uaWKxm9i3oqBQmI361ZlV81CXwf/HgVmK8C/nBkRrvPbXoNG88dFO6bXZHRhqqmusaAiWRqo/INvI0Ykfrx9zGtWoWDmG8LmigrS9r31q9r1YENQshlw1vLnBlsRHoK4S3fj+AnIqz5W/H4RBf92ik6VgmTwmERIDXUryJO6uZKLaMnXm9yYYgkSE3CJd91tmiIeR92jBb3b8hF5Pm1kyTK6qW7GsdA2ybnC4ueez9qmxosW5kRh6I+PEw8HCxiBno6qeXb4e6p0pgYL38oz+yhfmoRWlW|sqY0adRCWGB/CE2viadPBGBBbaHCAe/V4KFwr8eW/08=|10|51987c75976c595af8f6e5b793a7c623; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZFY=C:BtWlDYn2vvbhq54rjO:BevzXkLZNv:AbRA3Fah5VvMrA:C; BAIDUID_BFESS=EF08EE41A5B9911A97D741FCA1E975AB:FG=1; BAIDU_WISE_UID=wapp_1668931780429_949; MCITY=-%3A; __bid_n=18495ad43f144d83c64207; BK_SEARCHLOG=%7B%22key%22%3A%5B%22%E4%BC%9A%E4%BB%99%E5%96%80%E6%96%AF%E7%89%B9%E5%9B%BD%E5%AE%B6%E6%B9%BF%E5%9C%B0%E5%85%AC%E5%9B%AD%E6%99%AF%E5%8C%BA%22%2C%22%E6%A1%82%E6%9E%97%E6%BC%93%E6%B1%9F%E6%99%AF%E5%8C%BA%22%2C%22%E6%A1%82%E6%9E%97%22%2C%22%E6%A1%82%E6%9E%97%E4%B8%83%E6%98%9F%E5%85%AC%E5%9B%AD%22%2C%22%E8%B1%A1%E9%BC%BB%E5%B1%B1%22%2C%22%E7%94%A8%E6%B0%9F%E5%88%B7%E7%89%99%22%2C%22%E7%94%A8%E7%9A%84%E6%95%B0%E5%AD%97%E5%9B%BE%E5%83%8F%E7%9A%84%E8%B7%9D%E7%A6%BB%E5%BA%A6%E9%87%8F%E6%9C%89%E5%87%A0%E7%A7%8D%3F%22%5D%7D; BA_HECTOR=a42k85010084202104802vdd1hnpagk1e; delPer=0; PSINO=6; H_PS_PSSID=37784_36554_37552_37519_37772_37628_34813_37778_37819_37727_37793_37712_37742_26350_37789; zhishiTopicRequestTime=1669174887100; BDUSS=mt5NmljaFBnVUE5RGdxQVRvMEZCfklSS09NTkFVZ0FqTnNEa1hSflF3Si1JNlZqSUFBQUFBJCQAAAAAAAAAAAEAAABbpYyTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH6WfWN-ln1ja; BDUSS_BFESS=mt5NmljaFBnVUE5RGdxQVRvMEZCfklSS09NTkFVZ0FqTnNEa1hSflF3Si1JNlZqSUFBQUFBJCQAAAAAAAAAAAEAAABbpYyTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH6WfWN-ln1ja; channel=passport.baidu.com; baikeVisitId=5f33655f-41f8-474d-8e54-9589a8fa8510; RT='sl=8&ss=lat3mooz&tt=b4g&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&z=1&dm=baidu.com&si=1e981726-04a9-4146-be75-d83748eee7ca'; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1668564739,1668958469,1669132483,1669174993; Hm_lpvt_55b574651fcae74b0a9f1cf9c8d7c93a=1669174993; ab_sr=1.0.1_ZDE3M2EwZTU0MjIyMmU5ZjFlYjM0ODBjYTY4NzZkOGNmZTU5MDc0YWU4N2Y2ODhkNWNiMDRhNzE2YjQ5Mjg2ZmMyMGVjYTc4OTJmZjFjNWM3NzNiZTJlZTkyYjk3OTQ4NGE0YTNkZGExNzdkMjYzODAyMzMwNzBkYTgwYjJlYjE1NDdkOTM1OWYxYzg2ZWUzNDU0ZDVkNDA3MWJjYjI2ZmJmMWU2MWEwNjMzYTk5YTg2MDhmYTYxMzkwNjAwMDQx"
       }
       ip = "http://" + random.choice(ips)
       # response = requests.get(url, headers=header,proxies={"http":ip}, timeout=5)
       driver = webdriver.Chrome()
       driver.set_window_size(1280, 720)  # 自定义窗口大小：
       driver.implicitly_wait(3)  # 设置隐式时间等待
       driver.get(url)
       driver.implicitly_wait(3)  # 设置隐式时间等待
       data = driver.page_source
       try:
           like_count=driver.find_element(by='xpath',value="//*[@id='j-top-vote']/span[1]").text  #点赞数
           print(like_count)
           share_count=driver.find_element(by='xpath',value="//*[@id='j-topShareCount']").text #转发量
           print(share_count)
           see_count=driver.find_element(by='xpath',value="//*[@id='j-lemmaStatistics-pv']").text #浏览量
           print(see_count)
           edit_count_text=driver.find_element(by='xpath',value="/html/body/div[3]/div[2]/div/div[2]/dl/dd[1]/ul/li[2]").text #编辑量
           print(edit_count_text)
           num = re.findall(r"\d+", edit_count_text)
           print(num)
           edit_count = ""
           if num is not None:
               for content in num:
                   edit_count = edit_count + content
           print("搜索结果数",num)
           # 插入数据库
           update_sql = "UPDATE scenics SET bdword_url = %s where id = %s "
           insert_sql = "insert into bd_words(scenicId,scenicName,like_count,share_count,see_count,edit_count,crawlTime) values (%s,%s,%s,%s,%s,%s,%s)"
           update(update_sql, (url, id))
           insert(insert_sql, (id, kw, like_count,share_count,see_count,edit_count, datetime.date.today()))
           driver.close()
       except:
                print("暂未收录该词条")
                driver.close()


    def run(self):
        url_list = getRows("select id,name from scenics ", None)
        for content in url_list:
            print("爬取景点", content)
            id = content[0]
            kw = content[1]
            self.parse(id,kw)
# if __name__ =="__main__":
#     baiduWord=BaiDuWords()
#     baiduWord.run()