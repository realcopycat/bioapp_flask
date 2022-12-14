#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：爬虫 -> baidusearch
@IDE    ：PyCharm
@Author ：sandmswift
@Date   ：2022-11-15 18:11
@Desc
=================================================='''
from urllib import parse
import time
import random
import datetime
import re
import requests
from wangModel.utils.proxys import PROXY,ips
from lxml import etree
from wangModel.utils.HbaseConn import HbaseUtil
from wangModel.utils.mysqlConn import query,insert,getRows,update
"""
爬取百度搜索各个景点的搜索结果数量
"""
class BaiduSpider():

    def parse(self):
        kw=""
        url_list = getRows("select id,name from scenics ", None)
        for content in url_list:
            item={}
            print(content)
            time.sleep(random.randint(1,5))
            id=content[0]
            item['id']=id
            name=content[1]
            item['name']=name.strip()
            kw=parse.quote(name)
            url= f"https://www.baidu.com/s?wd={kw}&rsv_spt=1&rsv_iqid=0xd0a36e920005e207&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&rqlang=&tn=baiduhome_pg&ch="
            item['url']=url
            self.parse_item(url,item)

    def parse_item(self, url,item):
        print("--------------发起请求--------------------")
        header = {
            "Cipher-Text": "1668409355251_1668493173103_aLgQH4YFqAwPcYSE7v52xdJaHSAeId9tI+WY1JMiHu8HwngWY2DifDL8GwYz2O+DvIVgj+9ldrUsKJ3ADGdnEUHL1GARwcCChi73BbkUFeNFtACrNrwhmPStsz0iWKZEK1aqGImhb+zMQg9/qJkxFRR+4AuJz5zbU+IkH793cccuV18DONXlam0zLfF07BZFrBRtTFCC7P7YOpfz9du1sz0OHMxRr7Iwdq1hrNzZ0yW4pzm8Hw2C7gvEfXs81XQSHDeGOtaoZ/IQyn5QqCYSsGC47kiKIeEy2hOaGITVWj4wBHvNe//u+dxPX/cDPjIM7QWoQnmSAg2qOAUtzTMnBE0Eal21o3C03eGBGNJHXYM9xVQz2OEs+NeMG2HXjKi5boG4R8ypMvU8D5JsL9lU7G2WStNDiX7sEjaskomtx2g=",
            "Referer": "https://index.baidu.com/v2/main/index.html",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42",
            "Cookie": "BIDUPSID=B772A7AE03D22C237EA5162D657EFEA8; PSTM=1646828464; BAIDUID=EF08EE41A5B9911A97D741FCA1E975AB:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BCLID_BFESS=8610272839171174388; BDSFRCVID_BFESS=LqkOJeCmHx1yiQOjtw6fuaBrwgKK0gOTHbucfJLsovUqE2IVJeC6EG0Ptf8g0Kubdu1yogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJFfoK0afIK3f-opMtT5q4t3KxrjetJyaR3rQRvvWJ5TDqn9DJrE0f4q5htqKJQK0jrf0hvctn3cShnP5tbtyxAyhpjPbxLHWGcZ0l8K3l02V-bIe-t2ynLVbh_Dh4RMW20j0h7mWIQvsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJEjj6jK4JKjaK8t65P; delPer=0; PSINO=6; BA_HECTOR=200h85al2l2001agah0gat3a1hn62841f; BAIDUID_BFESS=EF08EE41A5B9911A97D741FCA1E975AB:FG=1; ZFY=PEntF3sipSTjFmSpBgjsg2if1PiObhH0XFP3GeQX4wg:C; H_PS_PSSID=37784_36554_37552_37519_37689_37772_37628_34813_37778_37727_37538_37712_37742_26350_37789; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1668491560; BDUSS=FZTkFXWlFOLVVLdjExR293ZXZQWXkyeXFzRzVUZll1OXo5azR0SjlueGd2SnBqSVFBQUFBJCQAAAAAAAAAAAEAAABbpYyTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAvc2NgL3NjOG; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a04185056022rfZ4Fr8b%2FZjzCjWhkEXzVhsU%2BRJmUfM92Rxqhej6x6RSy2D67EegK8bVq7Xw8G45FA9lGDxsArHhqi6FUXK4q4RUQKI%2FOaidfKoId7N9w5%2BvNtec2wUhywSQZq0jcgF6x9ekV4CZhLqqdSZJW8MmPYtfaFxQO1F04SU%2Bg1VM6k80VfstLewTJ%2FyvBssATejPpii0mplIhwrdv4izW0XcCSgczOv1KoEYf3DDBB%2BAkLlXIVuMXT08UND685c51gs1LPln6JVHlEmqjH2syDrFSw%3D%3D93823493866336522493836350719633; __cas__rn__=418505602; __cas__st__212=c3dabde61364b016ccd784a68f72be264e46b9a5983c1a499a1f2f58aed9b391b09413376c3a0f261c176a62; __cas__id__212=41971051; CPID_212=41971051; CPTK_212=693995330; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc=%7B%22uid_%22%3A%7B%22value%22%3A%222475468123%22%2C%22scope%22%3A1%7D%7D; bdindexid=t2n1cvnhg9lue59q0t78cq8jb2; RT='z=1&dm=baidu.com&si=524e125a-f181-40a3-b23b-0f6278b2185e&ss=lahssm1u&sl=f&tt=kfp&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf'; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1668493173; BDUSS_BFESS=FZTkFXWlFOLVVLdjExR293ZXZQWXkyeXFzRzVUZll1OXo5azR0SjlueGd2SnBqSVFBQUFBJCQAAAAAAAAAAAEAAABbpYyTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAvc2NgL3NjOG; ab_sr=1.0.1_ZTJlZDhiZWMyN2IxYWY2MjQ5NzZiNDVkODUyMTIwNzJlNWRmMjAyZWY2ZDFiYWVmNDE2ODE4ZmIyOTQ5MGZmNDdiNTQ5ODJjNWY1MGViN2MwOWI0YzEyYzBlZWY5NzU4MjM0ODk0NzFlMzUxNDJiZjI2ZDZiYWZlYzljMDAyMmZlNTM2MWUzMjdmYjY4MzA1YTAzMWE5MTdhODY1ZGZlYg=="
        }
        ip="http://"+random.choice(ips)
        response=requests.get(url,headers=header,proxies={"http":ip},timeout=5)
        selector = etree.HTML(response.text)
        try:
            data=selector.xpath("//*[@id='tsn_inner']/div[2]/span/text()")[0]
            num=re.findall(r"\d+",data)
            result=""
            if num is not None:
                for content in num:
                        result=result+content
            item['num']=result
            print(item)

            #插入数据库
            update_sql = "UPDATE scenics SET bdsearch_url = %s where id = %s "
            insert_sql = "insert into bd_search(scenicId,scenicName,num,crawlTime) values (%s,%s,%s,%s)"
            update(update_sql, (item['url'], item['id']))
            insert(insert_sql, (item['id'], item['name'], item['num'], datetime.date.today()))
        except:
            print("定位失败，检查Cokie是否失效或网页结构是否更改")
# if __name__ =="__main__":
#     run=BaiduSpider()
#     run.parse()