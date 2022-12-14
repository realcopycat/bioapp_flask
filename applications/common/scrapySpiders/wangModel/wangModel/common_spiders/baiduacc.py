#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：爬虫 -> baiduacc
@IDE    ：PyCharm
@Author ：sandmswift
@Date   ：2022-11-15 14:25
@Desc
=================================================='''
import json

import requests
from urllib import parse
import time
import random
from wangModel.utils.proxys import PROXY
from wangModel.utils.HbaseConn import HbaseUtil
import asyncio
import datetime
from wangModel.utils.mysqlConn import insert,query
import aiohttp
import time
class baiduacc():
    header = {
        "Cipher-Text":"1669014148691_1669025682395_gmyeUYFkqtWGz/Aodu6MCBx/jA/TcFYa3elCcC4PVE1i1F2XCekER0aqy9Mx1dO6Qu0Y3W2+6/ojulveu+uCC/Q1oRpRM2Iy/3YW0Dt7KogYgCtBAZulpY0RDu+dn5RiBs75lW9Ot/YIIeM4Pw5Bvtj6gwMLHLTS60hqu+o9xQdbJOQa8Dj3F2+Zyz+MXvMx1o4wulS5d/W8pIdT9n+Ud1J8ULkr3zIW2/dNMcX/53VET1S9IiG2uaG+3XDvf8rQLT8wIXKI9LwrwFI4+gZZhd/YnOMSb7reDLOo5bcfNyYRGzqpNb2Dozufe4HjuPzbvccAPU9XNigUDNyR/y5aqVUILehLWBs/bNg9OpuhvCsVumPQl/dIIDa57SKBBOHqSAx31TxH1po65FrdwblPhZF4qB9jXX/IzU1inyHNeKI=",
        "Accept":"application/json,text/plain,*/*",
        "Accept-Encoding":"gzip,deflate,br",
        "Accept-Language":"keep-alive",
        "Content-Length":"0",
        "Host":"index.baidu.com",
        "Origin":"https://index.baidu.com",
        "sec-ch-ua":"'Microsoft Edge';v='107', 'Chromium';v='107', 'Not=A?Brand';v='24'",
        "Referer":"https://index.baidu.com/v2/main/index.html",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52",
        "Cookie":"BIDUPSID=B772A7AE03D22C237EA5162D657EFEA8; PSTM=1646828464; ab_jid=1b5f1f7bd0d2ad6c8322197428813831b876; ab_jid_BFESS=1b5f1f7bd0d2ad6c8322197428813831b876; BAIDUID=EF08EE41A5B9911A97D741FCA1E975AB:FG=1; H_WISE_SIDS=110085_131862_188746_194529_204904_211986_212295_213039_214795_215730_216853_216941_219623_219943_219946_222624_223064_223337_224045_224047_224436_226628_226815_227932_228650_228870_229154_229907_229967_230077_230241_230244_230248_230287_230930_231433_231628_231761_231904_231979_232055_232244_232357_232616_232755_232834_232908_233041_233368_233401_233464_233465_233518_233598_233604_233719_233924_234044_234085_234208_234225_234296_234317_234349_234382_234515_234521_234559_234670_234690_234722_234799_234924_234980_235091_235131_235174_235201_235228_235258_235398_235421_235453_235461_235511_235534_235581_235634_235770_235808_235829_235870_235969_235980_236022_236050_236052_236084_236101_236129_236239_236243_236341_236512_236515_236524_236527_236538_236611_236811_236838; MCITY=-142%3A; delPer=0; PSINO=6; BAIDUID_BFESS=EF08EE41A5B9911A97D741FCA1E975AB:FG=1; BA_HECTOR=aha5208la10kagah8lak0qlp1ho93q81f; ZFY=xtXF:ABfiWEAgoaeInpi6iku9vkiVh7JUT1fVvaM9stc:C; bdindexid=p0k1jlaqpura3afsp3oajf1j73; BCLID=6870042325976552650; BCLID_BFESS=6870042325976552650; BDSFRCVID=J70OJexroG0leprj73-kMHDF9QpWxY5TDYrELPfiaimDVu-VJeC6EG0Pts1-dEu-EHtdogKKBgOTH4FF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=J70OJexroG0leprj73-kMHDF9QpWxY5TDYrELPfiaimDVu-VJeC6EG0Pts1-dEu-EHtdogKKBgOTH4FF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tbP8oK-MJKD3fP36q47HMtu_hlrt2D62aKDs3qTYBhcqEIL4Mj5E-P_wMGJ3Jp5uWgnlVlvVfx_bMUbSjln_0J_JhHon2nQwanrU_DD5yq5nhMJpXj7JDMP0XJbK35Oy523i5J3vQpPMslQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xb6_0DjPthxO-hI6aKC5bL6rJabC3OC0xXU6q2bDeQN3QKROH2JkesRvzWpbPbfjx3n7Zjq0vWq54WpOh2C60WlbCb664OR5JjxonDh83KNLLKUQtHmT7LnbO5hvvER3O3MAMQxKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRCf_IKM3e; H_BDCLCKID_SF_BFESS=tbP8oK-MJKD3fP36q47HMtu_hlrt2D62aKDs3qTYBhcqEIL4Mj5E-P_wMGJ3Jp5uWgnlVlvVfx_bMUbSjln_0J_JhHon2nQwanrU_DD5yq5nhMJpXj7JDMP0XJbK35Oy523i5J3vQpPMslQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xb6_0DjPthxO-hI6aKC5bL6rJabC3OC0xXU6q2bDeQN3QKROH2JkesRvzWpbPbfjx3n7Zjq0vWq54WpOh2C60WlbCb664OR5JjxonDh83KNLLKUQtHmT7LnbO5hvvER3O3MAMQxKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRCf_IKM3e; BDRCVFR[SquYicL8Vkb]=I67x6TjHwwYf0; H_PS_PSSID=26350; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; ZD_ENTRY=baidu; H_WISE_SIDS_BFESS=110085_131862_188746_194529_204904_211986_212295_213039_214795_215730_216853_216941_219623_219943_219946_222624_223064_223337_224045_224047_224436_226628_226815_227932_228650_228870_229154_229907_229967_230077_230241_230244_230248_230287_230930_231433_231628_231761_231904_231979_232055_232244_232357_232616_232755_232834_232908_233041_233368_233401_233464_233465_233518_233598_233604_233719_233924_234044_234085_234208_234225_234296_234317_234349_234382_234515_234521_234559_234670_234690_234722_234799_234924_234980_235091_235131_235174_235201_235228_235258_235398_235421_235453_235461_235511_235534_235581_235634_235770_235808_235829_235870_235969_235980_236022_236050_236052_236084_236101_236129_236239_236243_236341_236512_236515_236524_236527_236538_236611_236811_236838; __bid_n=1841d0d39462b7eb984207; BDUSS=VRCZDNtbXNuNW41UGlFbjZKUmI3WEc2aUxYYVFsejg0SVVROEVJNmtxd35SNnhqSUFBQUFBJCQAAAAAAAAAAAEAAAC67J41AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD-6hGM~uoRjY; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a04196552899imlBp2YPGD4aewP8FEYzgkEScKOqh7wb51tJTuP1B6MtmB3vSB6esoqA1w0BCKHaSr3H%2BaAs%2B95UgUw5JUbwAjHo4ooV%2BHBPtHJbiiJxU3CbQrkyxr2V65CIOTGVbPwt0Kij485ztLZlqLDr%2FeP4j8mK%2F1BnLMUjD0IZINAdz9OcGDB5KlDUGhEMUmHW5FkAhu26dh63%2FP000Cmpeyz06Ww6TciYJ3j7g9b1pdBcgCvDfrwAp4NUZ7z4PY8wFikBxuF2%2B0HT3niFFIDJz6HNM1GEJXoPVe0hWKEwKigxDYQ%3D80937910607250753648874982969453; ab_bid=4039c07e99dd9dfa4f512beb01a097f2a6ff; ab_sr=1.0.1_ZGMwYzg4NTQxY2U2MWM0OGY2ZmMzMzc3YmI2NzJlZDQ5NGQyNDc5NGI5NWJmYjMwZWUyMjBiYmU0MGFlOTc5YmM0MzEyNGI0ZDQxNjQ1YjNmY2M2YTEyYTliMWVjZGFjMjZhZDdkMmQ0YWM2NTM4Zjc4YTIwODNkNjY5YmQ4MzMwNjI5MDI1Yzc1OTZmMzUyYzFkNzEwYTcxYzQzZDAyYw==; RT='z=1&dm=baidu.com&si=630f2482-3780-4da8-9234-e06ac91171fd&ss=lb0u05kx&sl=m&tt=kt4&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf'; BDUSS_BFESS=VRCZDNtbXNuNW41UGlFbjZKUmI3WEc2aUxYYVFsejg0SVVROEVJNmtxd35SNnhqSUFBQUFBJCQAAAAAAAAAAAEAAAC67J41AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD-6hGM~uoRjY"
    }

    item_list=[]

    def __init__(self):
        host = '202.193.53.106'
        table_name = 'bauduacc'
        hbase = HbaseUtil(host)
        self.hbase = hbase
        self.tablename= table_name



    def parse1(self):
        time.sleep(3)
        try:
            url_list = query("select id,name,bdacc_url from scenics where bdacc_url !='' ", None)
            for redatas in url_list:
                id=redatas['id']
                scenicName=redatas['name']
                url=redatas['url']
                # url = f"https://index.baidu.com/api/SearchApi/index?area=0&word=[[%7B%22name%22:%22{parse.quote(keyword)}%22,%22wordType%22:1%7D]]&days=30"

                response = requests.get(url, headers=self.header, proxies=PROXY, timeout=5)
                time.sleep(3)
                data= response.json()
                if data['data'] =='':
                    # print(data)
                    print("被检测了，请更新验证数据")
                else:
                    print(data['data'])
                    start_time=str(data['data']['userIndexes'][0]['all']['startDate'])
                    end_time=str(data['data']['userIndexes'][0]['all']['endDate'])
                    all_avg=str(data['data']['generalRatio'][0]['all']['avg']) #整体日均值
                    all_yoy=str(data['data']['generalRatio'][0]['all']['yoy'])+"%" #整体同比%
                    all_qoq=str(data['data']['generalRatio'][0]['all']['qoq'] )+"%"#整体环比%
                    wise_avg=str(data['data']['generalRatio'][0]['wise']['avg'] )+"%"#移动日均值
                    wise_yoy=str(data['data']['generalRatio'][0]['wise']['yoy'] )+"%"#移动同比%
                    wise_qoq=str(data['data']['generalRatio'][0]['wise']['qoq'] )+"%"#移动环比%

                    sql="INSERT INTO baiduacc(scenicId,all_avg,all_yoy,all_qoq,wise_avg,wise_yoy,wise_qoq,crawlTime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
                    insert(sql,(id,all_avg,all_yoy,all_qoq,wise_avg,wise_yoy,wise_qoq,datetime.date.today()))
        except:
            print("url无效")
    #
    # def inputHbase(self,list):
    #     for i in range(len(list)):
    #         # 插入数据库
    #         print(list[i])
    #         self.hbase.putTable(self.tablename, str(datetime.date.today())+"_"+str(i), {
    #             'info:name': list[i]['name'],
    #             'all:all_avg': list[i]['all_avg'],
    #             'all:all_yoy': list[i]['all_yoy'],
    #             'all:all_qoq': list[i]['all_qoq'],
    #             'wise:wise_avg': list[i]['wise_avg'],
    #             'wise:wise_yoy': list[i]['wise_yoy'],
    #             'wise:wise_qoq': list[i]['wise_qoq'],
    #         })

# if __name__=="__main__":
#
#     object=baiduacc()
#     object.parse1()


