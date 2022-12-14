import re
import time
import requests
import aiohttp
import asyncio
import json
#评论内容所在的url，？后面是get请求需要的参数内容
comment_url='http://pagelet.mafengwo.cn/poi/pagelet/poiCommentListApi?'

headers={
    'Referer': 'https://www.mafengwo.cn/jd/10095/gonglve.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}#请求头

from datetime import date, timedelta
today = time.strftime("%Y-%m-%d", time.localtime())
tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")

from MysqlConnect import *
mysql = MysqlConnect()
mysqlTableName = "hotels"

class Mafengwo_Scenic:
    async def getComment(self,item,session):
        try:
            # async with session.post(item["url"]) as res:
            # resp = await res.content()
            resp = requests.post(item['url'],headers=eval(item['headers']))
            page = resp.content.decode('unicode-escape', 'ignore').encode('utf-8', 'ignore').decode('utf-8')#爬取页面并且解码
            page = page.replace('\/', '/')#将\/转换成/
            # print(page)
            # 评论数量
            commentCountRes = re.compile(r'共有<em>(?P<commentCount>.*?)</em>').search(page)
            commentCount = commentCountRes.group('commentCount')
            # 评论标题
            nameobj = re.compile(r'<a href="javascript:void\(0\);">(?P<tag>.*?)</span>',re.S)
            tagList = nameobj.findall(page)
            # 评论数量
            numobj = re.compile(r'<span class="num">(?P<num>.*?)</span>',re.S)
            numList = numobj.findall(page)
            othersComment = []
            dic = {"好评":0,"中评":0,"差评":0}
            for i in range(0,len(numList)):
                # 处理标题
                tag = str(tagList[i+1])
                tag = tag.replace('\n','').replace('<span>','').strip().replace('人提及）','').replace('<span class="num">（','')
                tag = re.sub(r'[0-9]+', '', tag)
                # 处理数量
                num = str(numList[i])
                num = num.replace('（','').replace('）','').replace('条','').replace('人提及','').replace(' (','').replace(')','')

                if tag != "好评" and tag != "中评"'' and tag != "差评":
                    othersComment.append({f"{tag}": num})
                else:
                    dic[f"{tag}"] = num
            othersComment = str(othersComment)
            args = (
                item["id"], item["name"], commentCount, dic["好评"], dic["中评"], dic["差评"], othersComment,
                today, "马蜂窝")
            print(args)
            sql = f'INSERT INTO scenic_comment(scenicId,scenicName,num,good,middle,bad,othersComment,crawlTime,siteFrom) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            mysql.insert(sql, args)
        except Exception as e:
            print("comment报错",e)

    async def saveScenic(self):
        for i in range(1,2):
            url = "https://www.mafengwo.cn/ajax/router.php"
            data = {
                'sAct':"KMdd_StructWebAjax|GetPoisByTag",
                'iMddid':"10095",
                'iTagId':"0",
                'iPage':20,
                '_ts':"1669286358348",
                '_sn':"69d4a7c89e"
            }
            try:
                res = requests.post(url, headers=headers, data=data)
                # print(res.json())
                List = re.compile(r'/poi/(.*?).html.*?target="_blank" title="(.*?)">').findall(str(res.json()))
                # print(List)
                for item in List:
                    mfw_url = 'https://pagelet.mafengwo.cn/poi/pagelet/poiCommentListApi?callback=jQuery1810866662618942958_1669200603971&params={"poi_id":"%s","page":1}&_ts=1669200604147&_sn=8e0384d86d&_=1669200604147' % (
                    item[0])
                    mfw_headers = {
                        'Referer': f'http://www.mafengwo.cn/poi/{item[0]}.html',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
                    }
                    args = (mfw_url, json.dumps(mfw_headers), today, item[1])
                    print(args)
                if i % 5 == 0:
                    time.sleep(5)
            except Exception as e:
                print(e)

    async def getScenic(self):
        results = mysql.query("select id,name,mfw_url,mfw_header from scenics where mfw_url !='' ", None)
        tasks = []
        url_list = []
        for row in results:
            id = row[0]
            name = row[1]
            url = row[2]
            headers = row[3]
            url_list.append({
                "id": id,
                "name": name,
                "url": url,
                "headers": headers,
            })
        print("马蜂窝网站的所有景区长度",len(url_list))
        i = 0
        for item in url_list:
            async with aiohttp.ClientSession(headers=eval(item['headers'])) as session:
                task1 = asyncio.create_task(self.getComment(item, session))
                i = i + 1
                tasks.append(task1)
                if i % 5 == 0 :
                    time.sleep(5)
                await asyncio.wait(tasks)
        # 关闭mysql
        mysql.cur.close()
        mysql.connection.close()

if __name__ == '__main__':
    asyncio.run(getScenic())
    # asyncio.run(saveScenic())
