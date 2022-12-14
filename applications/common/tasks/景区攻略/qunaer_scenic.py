import requests
import re
import aiohttp
import asyncio
import os
import xlwt
import xlrd
import time
import random
import json
import openpyxl

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
    # "Cookie": 'QN1=00009180306c48f75230434f; QN300=s%3Dbaidu; QN99=7930; QunarGlobal=10.67.197.57_-315863c_1844fb4402c_-4886|1667785799221; QN205=s%3Dbaidu; QN277=s%3Dbaidu; _i=ueHd8Zy9S8X7Cs5y-nPVKDLNsGkX; QN601=fc3340e635beebd8fed01d244dfa103f; QN269=7D87F9C05E3E11ED8278FA163EAD537B; QN48=tc_b56d9b243d79884d_1844fc7bd55_d0d9; fid=ab2cfc1a-4442-4996-8058-95e369865862; csrfToken=vwiqxqLdRWrdSUvmIn84yliNXbhGLphE; QN58=1669821195055%7C1669822256665%7C5; QN57=16678736048620.2656904960064569; ctt_june=1654604625968##iK3wVRvNVhPwawPwa%3DjnWRa%2BES2Aa2PwW2aOaS0RE2DsEDGDE2DsERfIXSX8iK3siK3saKjOWst%2BWR3sWRX8VuPwaUvt; ctf_june=1654604625968##iK3wWsaOWwPwawPwa%3DkhWDfTaD3NXsERXKj%3DX2EGEKaAWs28aSERW2a%3DWsX%2BiK3siK3saKjOVK2%2BWK2AWRamVhPwaUvt; cs_june=1e980219e0683d534a30d19cbf460690504831204710eca7ff8957e47452ae78150e2f38a8a12ca96514b111ebdac1878f7fa30cb8f280132faaa5b783ecd9d7b17c80df7eee7c02a9c1a6a5b97c1179774d0c3f26f472d208f55073055c8e3b5a737ae180251ef5be23400b098dd8ca; QN271AC=register_pc; QN271SL=791c41e753d68b5ac9365b726bb2960d; QN271RC=791c41e753d68b5ac9365b726bb2960d; Hm_lvt_c56a2b5278263aa647778d304009eafc=1667874629,1668075379,1669972940; viewpoi=5942247|716544|706160|722948; uld=1-300113-1-1669974575|1-299801-3-1669974326|2-5942247-1-1667874649; SECKEY_ABVK=oBn0fel6+CD+aAN/hYsF0tz2y0FKgx63zX5Zn2S9lEM%3D; BMAP_SECKEY=6322QfSPZ1N2m2UuiZlS0H6FoMDxhQ-GnPPIgN-EndoROx7_vGs84WwiwKWL44NBDiCLOGD2d-Y7KyqD2s8PM2ytpXq2q1eZ0TzXIPrmUoDe2ij4Z5mR9gOY1KAWi2msFlzCCbX6sugCEQBjlDn83Ly8gGRLDqMpqMWaTSICD2NztE1Tawzv3BAgu-x7EUlO; QN233=FreetripTouchin; HN1=v1ecbd83e6109eb406ad7ee9754047124a; HN2=qunuqnuggzkcg; quinn=e5ba94e400db7ae611b28097b8ad7ddc9fea18aa074280921e89258cf82e7cb417cc1fc89ba3f04bfda0535faf80ae42; QN621=1490067914133%2Ctestssong%3DDEFAULT%26fr%3Dtejia_inton_search%261490067914133%252Ctestssong%3DDEFAULT; QN668=51%2C56%2C56%2C58%2C56%2C55%2C54%2C56%2C58%2C57%2C57%2C51%2C56; QN243=679; ariaDefaultTheme=null; QN100=WyLotaDnq7nnrZLppa3ppa7nlKjmsLTmoYLmnpfpvpnohIrmoq%2FnlLDph5HlnZHlpKflr6jpu4TmtJvnkbblr6jlpKflt7Tovabnuq%2Fnjqnlj6%2FliqDnvIbovabkuIDml6XmuLh85qGC5p6XIiwi5Yid6YGH5ryT5rGf55WF5ri457K%2B576O5ryT5rGf57K%2B5Y2O5ri46Ii56KeC6LWP5LqM5Y2B5YWD5Lq65rCR5biB6IOM5pmv5Lmd6ams55S75bGx5b6S5q2l5YW05Z2q5Y%2Bk6ZWH6Ziz5pyU5LiW55WM5rq25rSe5aWH6KeC6ZO25a2Q5bKp57qv546p5LiA5pel5ri4fOahguaelyIsIuahguael%2BmYs%2BaclOe6r%2BeOqeS4gOaXpea4uOmTtuWtkOWyqeaXoOi0reeJqXzmoYLmnpciLCLng63ojZAxMuS6uueyvuWTgeWwj%2BWboiDmvJPmsZ%2FmuLjoiLkyMOWFg%2BiDjOaZr%2BmBh%2Bm%2Bmeays%2BmTtuWtkOWyqeWNgXzmoYLmnpciLCLmoYLmnpd85qGC5p6XIl0%3D; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; QN267=0531040385eb6753d; QN271=aac3c78a-6161-4135-8024-4d417d4798fd; JSESSIONID=540F1DB1B565507C76E711DE50DEEE27; Hm_lpvt_c56a2b5278263aa647778d304009eafc=1669976262; viewdist=299801-1; viewbook=7673685|5804838|7405861; _vi=oVDC9e1VW3oiCf8HuMZBgBCq212ulsphL4ZvksnfyM24u9ptCRpd6nwZ_dl356Rh70BPTkTu65nuFpEFZTuI0pekzVy6x6EWIVwDrft6xlPPMZ0c2DO6nWnwUxB0zc_J36j7pNWamepyavD-W6SanJmZzLr59gUrgIrbH3thSQUe'
}
# 获取当前时间
from datetime import date, timedelta

today = time.strftime("%Y-%m-%d", time.localtime())
tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")

from MysqlConnect import *

mysql = MysqlConnect()

class Qunaer_Scenic:
    async def getGuild(self,item, session):
        try:
            async with session.get(item["start_heat"]) as res:
                resp = await res.text()
                start_heat = 0
                result = re.compile(r'data-beacon="tab_gonglue">攻略 \((.*?)\)</a>').findall(resp)
                if result != []:
                    start_heat = result[0]
            async with session.get(item["elite_heat"]) as res:
                resp = await res.text()
                elite_heat = 0
                result = re.compile(r'data-beacon="tab_gonglue">攻略 \((.*?)\)</a>').findall(resp)
                if result != []:
                    elite_heat = result[0]
            async with session.get(item["hot_heat"]) as res:
                resp = await res.text()
                hot_heat = 0
                result = re.compile(r'data-beacon="tab_gonglue">攻略 \((.*?)\)</a>').findall(resp)
                if result != []:
                    hot_heat = result[0]
                args = (item["id"], item["name"], start_heat, elite_heat, hot_heat, today, "去哪儿")
                print(args)
                # sql = f'INSERT INTO scenic_index(scenicId,scenic_name,guide_num,elite_guide_num_num,hot_guide_num,crawlTime,siteFrom) VALUES(%s,%s,%s,%s,%s,%s,%s);'
                # mysql.insert(sql, args)

        except Exception as e:
            print("comment报错", e)
            # print(item)
            # print("报错页数",index,sightId)


    async def getScenic(self):
        async with aiohttp.ClientSession(headers=headers) as session:
            results = mysql.query("select id,name,gw_url from scenics where gw_url !='' ", None)
            tasks = []
            url_list = []
            for row in results:
                id = row[0]
                name = row[1]
                url = row[2]
                url_list.append({
                    "id": id,
                    "name": name,
                    "url": url,
                })
            print("去哪儿网站的所有景区长度", len(url_list))
            for item in url_list:
                item['start_heat'] = f"https://travel.qunar.com/search/gonglue/{item['name']}/start_heat/1.htm"
                item['elite_heat'] = f"https://travel.qunar.com/search/gonglue/{item['name']}/elite_heat/1.htm"
                item['hot_heat'] = f"https://travel.qunar.com/search/gonglue/{item['name']}/hot_heat/1.htm"
                task = asyncio.create_task(self.getGuild(item, session))
                tasks.append(task)
                await asyncio.wait(tasks)
                # time.sleep(5)
            # 关闭mysql
            mysql.cur.close()
            mysql.connection.close()



if __name__ == "__main__":
    asyncio.run(getScenic())
