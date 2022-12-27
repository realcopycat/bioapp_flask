import requests
import re
import aiohttp
import asyncio
import csv
import json
import os
import time
import datetime
import pytz
from lxml import etree
import time
from wangModel.utils.proxys import PROXY
from parsel import Selector
from wangModel.utils.mysqlConn import insert


from datetime import date, timedelta

today = time.strftime("%Y-%m-%d", time.localtime())
tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
headers = {
    'Referer':"https://www.tuniu.com/",
    'User-Agent':'Mozilla/5.0(Windows NT 10.0; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46',
    'Cookie': "_uab_collina=166113651603660325791145; udid=tn-100-1661136526886-f196ed1d-21c4-11ed-921a-0ba79eabb6b9; _tact=ODE2YWU2MjgtMDU4MC1hYzJjLTQwOWMtMDMyZGEyNzIzMTMz; _ga=GA1.2.2105264209.1661136529; p_phone_400=4007-999-999; p_phone_level=0; p_global_phone=%2B0086-25-8685-9999; fp_ver=4.7.3; BSFIT_OkLJUJ=FHMgfFXHnQXEiVkz8qQ3cNf9ukZQWypQ; cto_bundle=DDPyZ19ENHlVa1poTVJiZ0twWTExWTB1WXF3RUZzQm5wQjB4c1d0cUsycCUyQkpQMkdFdkVnNnhtcXEzbkZmTW1zYnJCcFBHa3FSWlNKOFVyJTJCN2NJSVkxdWxLTDU0MENscU5QRnhNZHVPZFZiU0h1dHpVcXdlWkJNaE9mcGhOUnQ1STBNTlBnQ1FLREtZN09OMXV1YmJQanZUeHF3JTNEJTNE; __utmz=1.1668932705.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_44f54d76a67ba9230a7bb92d5ed5e4ba=1667808931,1668142577,1668940349; __utma=1.2105264209.1661136529.1668958304.1668962727.6; tuniuuser_force_logout=1669109601000; tuniuuser_vip=MA%3D%3D; tuniuuser_level=MA%3D%3D; tuniuuser_id=97164384; tuniuuser_name=MTUyMjkyMzI1Mw%3D%3D; tuniuuser_image=Ly9pbWczLnR1bml1Y2RuLmNvbS9pbWcvMjAxNDA0MDkwMS91c2VyX2NlbnRlci9nX3RvdXhpYW5nLnBuZw%3D%3D; _tacz2=taccsr%3Dcn.bing.com%7Ctacccn%3D%28referral%29%7Ctaccmd%3D%28none%29%7Ctaccct%3D%28none%29%7Ctaccrt%3D%28none%29; tuniu_partner=MTAxLDAsLDlmZDgyZThjYTZkNGMwMTlmZTUyNzdlYjJmNTcxYzQ1; isHaveShowPriceTips=1; _tacau=MCw4NjMxMDNiZi1kOGIwLTViMmYtMWZlMS1mNTFjYjYzYjgyNDIs; PageSwitch=1%2C213612736; _gid=GA1.2.387299839.1670741383; clickCache=%5B%7B%22key%22%3A1670741382627%2C%22url%22%3A%22https%3A%2F%2Fwww.tuniu.com%2F%22%2C%22pageName%22%3A%22%E5%BA%A6%E5%81%87%3A%E5%8D%97%E5%AE%81%3A%E9%A6%96%E9%A1%B5%3Ann%22%2C%22referer%22%3A%22%22%2C%22events%22%3A%5B%7B%22text%22%3A%22%E7%82%B9%E5%87%BB_%E9%A1%B6%E9%83%A8%E5%AF%BC%E8%88%AA_%E4%B8%80%E7%BA%A7%E5%AF%BC%E8%88%AA_6_%E9%85%92%E5%BA%97%22%2C%22x%22%3A394%2C%22y%22%3A149%2C%22lg%22%3A1670741384382%7D%5D%7D%5D; rg_entrance=010000%2F003001%2F000013%2F000000; tuniu-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22bgcolor%22:false}; Hm_lvt_fe3fbe4228e14b1544525f058df92f91=1669634420,1670140045,1670741377,1670757948; _pzfxuvpc=1661136528944%7C9947719618884716956%7C135%7C1670757948543%7C48%7C1145071184993068063%7C2602933339806650760; OLBSESSID=m10d18uckfquipe2llgnec7ds4; acw_sc__v2=6395be40a848e7c226787a31326638850a340bc0; tuniu_zeus=M18zXzFfMV8xXzI6Omh0dHBzOi8vbWVucGlhby50dW5pdS5jb20vOjoyMDIyLTExLTIwIDIyOjIzOjQy%2CM18zXzFfMV8xXzI6Omh0dHBzOi8vdHJpcHMudHVuaXUuY29tLzo6MjAyMi0xMS0yMCAyMjozMDo0Mw%3D%3D%2CM18zXzFfMV8xXzI6Omh0dHBzOi8vbWVucGlhby50dW5pdS5jb20vOjoyMDIyLTExLTIwIDIyOjMwOjQ5%2CM18zXzFfMV8xXzI6Omh0dHBzOi8vd3d3LnR1bml1LmNvbS86OjIwMjItMTEtMjAgMjM6MTA6MDQ%3D%2CM18zXzFfMV8xXzI6Omh0dHBzOi8vbWVucGlhby50dW5pdS5jb20vOjoyMDIyLTExLTIwIDIzOjI3OjM2%2CM18zXzFfMV8xXzI6Omh0dHBzOi8vbWVucGlhby50dW5pdS5jb20vOjoyMDIyLTExLTIxIDEyOjQ2OjUz%2CM18zXzFfMV8xXzI6Omh0dHBzOi8vbWVucGlhby50dW5pdS5jb20vOjoyMDIyLTExLTIxIDEyOjQ2OjU0%2CM18zXzFfMV8xXzI6Omh0dHBzOi8vd3d3LnR1bml1LmNvbS86OjIwMjItMTEtMjEgMTY6MjI6MjU%3D%2CM18zXzFfMV8xXzI6Omh0dHBzOi8vbWVucGlhby50dW5pdS5jb20vOjoyMDIyLTExLTIxIDE2OjIyOjQz%2CM18zXzFfMV8xXzI6Omh0dHBzOi8vd3d3LnR1bml1LmNvbS90b3Vycy86OjIwMjItMTItMTEgMTk6MjU6NTI%3D%2CM18zXzFfMV8xXzI6Omh0dHBzOi8vd3d3LnR1bml1LmNvbS90b3Vycy86OjIwMjItMTItMTEgMTk6MjU6NTU%3D; tuniu_searched=a%3A5%3A%7Bi%3A0%3Ba%3A2%3A%7Bs%3A7%3A%22keyword%22%3Bs%3A6%3A%22%E6%A1%82%E6%9E%97%22%3Bs%3A4%3A%22link%22%3Bs%3A47%3A%22%2F%2Fs.tuniu.com%2Fsearch_complex%2Ftours-nn-0-%E6%A1%82%E6%9E%97%2F%22%3B%7Di%3A1%3Ba%3A2%3A%7Bs%3A7%3A%22keyword%22%3Bs%3A21%3A%22%E6%A1%82%E6%9E%97%E7%9A%84%E6%97%85%E6%B8%B8%E7%BA%BF%E8%B7%AF%22%3Bs%3A4%3A%22link%22%3Bs%3A50%3A%22http%3A%2F%2Fwww.tuniu.com%2Fg705%2Fwhole-gl-0%2Flist-h0-j0_0%2F%22%3B%7Di%3A2%3Ba%3A2%3A%7Bs%3A7%3A%22keyword%22%3Bs%3A62%3A%22%E8%AF%97%E4%B8%8E%E8%BF%9C%E6%96%B9%C2%B7%E6%BC%93%E6%B1%9F%E9%99%A2%E5%AD%90%E9%85%92%E5%BA%97%EF%BC%88%E4%B8%A4%E6%B1%9F%E5%9B%9B%E6%B9%96%E4%B8%9C%E8%A5%BF%E5%B7%B7%E5%BA%97%EF%BC%89%22%3Bs%3A4%3A%22link%22%3Bs%3A40%3A%22http%3A%2F%2Fhotel.tuniu.com%2Fdetail%2F2073760650%22%3B%7Di%3A3%3Ba%3A2%3A%7Bs%3A7%3A%22keyword%22%3Bs%3A58%3A%22%E8%AF%97%E4%B8%8E%E8%BF%9C%E6%96%B9%C2%B7%E6%BC%93%E6%B1%9F%E9%99%A2%E5%AD%90%E9%85%92%E5%BA%97%28%E4%B8%A4%E6%B1%9F%E5%9B%9B%E6%B9%96%E4%B8%9C%E8%A5%BF%E5%B7%B7%E5%BA%97%29%22%3Bs%3A4%3A%22link%22%3Bs%3A106%3A%22http%3A%2F%2Fs.tuniu.com%2Fsearch_complex%2Fhotel-gl-0-%E8%AF%97%E4%B8%8E%E8%BF%9C%E6%96%B9+%E6%BC%93%E6%B1%9F%E9%99%A2%E5%AD%90+%E4%B8%A4%E6%B1%9F%E5%9B%9B%E6%B9%96%E4%B8%9C%E8%A5%BF%E5%B7%B7%E5%BA%97%2F%3Fjump%3Dauto%22%3B%7Di%3A4%3Ba%3A2%3A%7Bs%3A7%3A%22keyword%22%3Bs%3A30%3A%22%E6%A1%82%E6%9E%97%E9%AB%98%E9%93%81%E5%8C%97%E7%AB%99%E4%BA%9A%E6%9C%B5%E9%85%92%E5%BA%97%22%3Bs%3A4%3A%22link%22%3Bs%3A71%3A%22%2F%2Fs.tuniu.com%2Fsearch_complex%2Fwhole-gl-0-%E6%A1%82%E6%9E%97%E9%AB%98%E9%93%81%E5%8C%97%E7%AB%99%E4%BA%9A%E6%9C%B5%E9%85%92%E5%BA%97%2F%22%3B%7D%7D; _taca=1661136526075.1670748191106.1670757961271.60; _tacb=NjcxMTdhMzMtNDYwNS0zMjE1LWI1MjUtMTc0NzEzMDI1YjM2; _tacc=1; Hm_lvt_51d49a7cda10d5dd86537755f081cc02=1669088113,1669636043,1670741377,1670757963; PcHomeVisit=1; BSFIT_EXPIRATION=1671968376330; BSFIT_DEVICEID=EJuL0zqYa9MeH-6Ld1C5FRNL8B1kMZYIegSialKv0NO8fko-n1BgNo4ADDsljSX9RDzQzUzxkgAzC-3ZltyyhA9ScDjMQi3oC6mV9IwloOamu0jnNiSVQErdw8ZDYB-HYu3jG6FqV1R30gENEORkYMaNBVfSo39z; tuniuuser_citycode=NzA1; tuniuuser_ip_citycode=NzA1; acw_tc=76b20f6216707597669104541e718761bbdb8491ea15506eaeb386802d1205; acw_sc__v3=6395c55b87a173d5c8ab0530eda85c313100aa8d; connect.sid=s%3ADVpFth7p1RAHGpm5xwz_qhKk2aNxKIEW.61uxobNGuz3FuYwMsUM4VC6yWaHU8%2FsMsdvUKjMO%2Bto; __xsptplusUT_352=1; Hm_lpvt_51d49a7cda10d5dd86537755f081cc02=1670759773; Hm_lpvt_fe3fbe4228e14b1544525f058df92f91=1670759773; __xsptplus352=352.28.1670758079.1670759773.5%234%7C%7C%7C%7C%7C%23%23x3KmvfCykhxF9YMlGHYyP86YcrS0s2BZ%23; ssxmod_itna2=GqAh7KY50KAIxYq0d4YKO1xUxDwUpAExacC1QDnFSiaPDs=55DLQury4qnbPWt=4=za2K63qzhLALHV7IBPx8MfgS0L1Vnbq4FCZS4qC2qiWbpOR6QHBmfa=Xf2=uCfNpN6UC95HwyrUaW7aeczFhcFFg9FNx71=I9rRr7kX6mCmrornmOvr9gvP6mkkFrpT+38p4STIYf=im4Dw22dDjKD+1d5i0r47g+KoYD==; ssxmod_itna=eqUxnDcD900Qit3GHIhCAYD7YA5xCDD5+LdD/KimDnqD=GFDK40oo7qr=oDOnBrAhnEG=UGAh+T+W7BWpxex1bqaTDU4i8DCLxNo+mDYY8Dt4DTD34DYDixibkxi5GRD0KDFF5XUZ9Dm4GWFqGfDDoDY86RDitD4qDBCodDKqGgFTxsFq2j7mt3pLxe57GcD0tdxBdeWawcGCcFciNe56nDNEQDzkHDtutS9kd3x0PyBMUDM2ozQi+1BoQebEhrz0D=bSOaiieN9/4rKODq8BCwj75cPD===Host: www.tuniu.comIf-None-Match: W/'3c-NfUtq77l6/q+4MT+i1B8akkKCJY'Referer: https://www.tuniu.com/tour/210484383?u_atoken=2a0c1736-73f1-4b7c-ad98-d6d94e03c5ab&u_asession=01903W2-YdH07896fdt57A6KHEQxoe3p_nM9u4UCHyFrbiLBWPB-i4K8FGDfX1dPGpX0KNBwm7Lovlpxjd_P_q4JsKWYrT3W_NKPr8w6oU7K9FEef24uNZxWMQdDwnHXnnD9UaPztW_A5jsQn1Dkg23WBkFo3NEHBv0PZUm6pbxQU&u_asig=0544d1nAGeRC20Zu086zLa4yldBmLJqPWv-B9mz-H9Xrtah9jkPouz-FPnXWOOi4UZ2dTfIGDG7nuzXDqJvJoeKGx9aDWVBLA6ECRzZSExcTnAgKFWx6KrKB261iRpf4DSkxMbgQTdrHv4qiNIfGkvC9dPO90Bbvr-EUj-WfwYHev9JS7q8ZD7Xtz2Ly-b0kmuyAKRFSVJkkdwVUnyHAIJzW5j2yf_d5xdXB-OIEbSd9cmnegWFHsFYePqrtdDZqCL5w-GOMIgInRzpzRYK0ZViu3h9VXwMyh6PgyDIVSG1W8a4h9Ftm1jXrxOtcF1nJf7yVBaI0FPIhiohXoTwrQ-uFvYeu4qtMWWYz3pQwg1DG_l-4EGHxB6fgv3zddmpOI2mWspDxyAEEo4kbsryBKb9Q&u_aref=zug78BonXAlUtdj%2FsdJ3FWivLgg%3D".encode('utf-8'),
}

route_list_pages=0

def temp():


    currentPage=1
    url = f"https://www.tuniu.com/g705/whole-gl-0/list-z9004399/{currentPage}"

    res = requests.get(url,headers=headers,proxies=PROXY)
    # print(res.text)
    selector = etree.HTML(res.text)

    #获取总页数
    allPage = selector.xpath("//*[@id='contentcontainer']/div[2]/div[1]/div[1]/div[2]/div/a[last()-1]/text()")
    print(allPage)
    if len(allPage)>0:
        print("页数", allPage)
        route_list_pages = int(allPage[0])
        time.sleep(2)

        for m in range(1,route_list_pages+1):
            currentPage=m
            res = requests.get(url, headers=headers, proxies=PROXY)
            selector = etree.HTML(res.text)
            list=selector.xpath("//*[@id='contentcontainer']/div[2]/div[1]/div[1]/div[1]/ul/li")

            print(len(list))
            for child in list:
                child_url=child.xpath("./div/a/@href")[0]   #线路详情链接
                title=child.xpath("./div/a/@aria-label")[0]
                scenics=child.xpath("./div/a/dl/dd[1]/@title")[0]
                print("路线",title)
                print("路线",type(title))
                print("景点",scenics)
                if child_url is not None:
                    time.sleep(3)
                    dedati_url="https:"+child_url

                    #解析线路详情
                    child_request=requests.get(dedati_url,headers=headers,proxies=PROXY)
                    childSelector=Selector(text=child_request.text)
                    routedesc=childSelector.css("#J_Detail > div > div.J_DetailRoute.section-box.detail-route.detail-route4 > div.section-box-body > div.J_DetailRouteDetail.section-box-content.detail-journey-4-detail.active > div.section-box-content.detail-route4-brief-box.detail-route4-brief-nomap > div > div > div")
                    print("这是爬取内容，如果没有就是被检测了",routedesc)
                    if routedesc:
                        routedesc=routedesc[0]
                        arranges_list=routedesc.xpath("./p")
                        desc=""
                        for i in range( len(arranges_list)):
                            content=routedesc.xpath(f"string(./p[{i}][@aria-label])").extract_first()
                            data=str(content).strip().replace(" ","").replace("\n","")
                            desc=desc+data+";"
                        print("简介",desc)
                        print(url)
                        sql = "INSERT INTO route(route_name,sceniclist,route_desc,tn_url) values (%s,%s,%s,%s);"
                        insert(sql,(str(title),scenics,desc,str(dedati_url)))

                        # #评价总数据
                        # try:
                        #     print(childSelector.xpath("//*[@id='J_Comment']/div/div[2]/div[2]/div[1]/div[2]/strong/text()"))
                        #     satistion=childSelector.xpath("//*[@id='J_Comment']/div/div[2]/div[2]/div[1]/div[2]/strong/text()").extract_first()
                        #     good=childSelector.xpath("//*[@id='J_Comment']/div/div[2]/div[2]/div[2]/div[1]/div[1]/text()").extract_first()
                        #     good=re.search("\d+",good).group()
                        #     middle=childSelector.xpath("//*[@id='J_Comment']/div/div[2]/div[2]/div[2]/div[2]/div[1]/text()").extract_first()
                        #     middle=re.search("\d+").group()
                        #     bad=childSelector.xpath("//*[@id='J_Comment']/div/div[2]/div[2]/div[2]/div[3]/div[1]/text()").extract_first()
                        #     bad=re.search("\d+",bad).group()
                        #     otherslist=childSelector.xpath("//*[@class='fraction']/div")
                        #     otherdata=[]
                        #     for otherService in otherslist:
                        #         service=otherService.xpath("./@aria-label")
                        #         print(service)
                        #         otherdata.append(service)
                        # except:
                        #     print("为获取渲染数据")


                    else:
                        print("网页爬虫被检测到了，请在网页手动验证")
    # # print(res.text)
if __name__ == '__main__':
    temp()
