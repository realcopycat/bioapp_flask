import time

import pymysql
import requests
from lxml import etree
import datetime
xiechengUrl = 'https://www.mafengwo.cn/search/q.php?q={}&t=notes&seid=8ADBD862-D2E8-4B0D-ADE1-0C98ED641130&mxid=&mid=&mname=&kt=1'


class Mafengwo_Scenic:

    def getSource(self,url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }

        response = requests.get(url,headers=headers)
        response.encoding = 'utf-8'
        return response.text

    def getEveryItem(self,id,name,source):
        try:
            html_element = etree.HTML(source)
            href_list = html_element.xpath('//*[@id="_j_mfw_search_main"]/div[1]/div/div/a/@href')

            guilde_url = href_list[2]
            note_url = href_list[3]
            answer_url = href_list[4]

            guilde_html = self.getSource(guilde_url)
            guilde_html = etree.HTML(guilde_html)
            note_html = self.getSource(note_url)
            note_html = etree.HTML(note_html)
            answer_html = self.getSource(answer_url)
            answer_html = etree.HTML(answer_html)

            guide_list = guilde_html.xpath('//*[@id="_j_search_result_left"]/div/div/ul/li')
            note_list = note_html.xpath('//*[@id="_j_search_result_left"]/div/div/ul/li')
            answer_list = answer_html.xpath('//*[@id="_j_search_result_left"]/div/div/div[@class="ct-text closeto"]')

            len_guide_list = len(guide_list)
            len_note_list = len(note_list)
            len_answer_list = len(answer_list)

            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            infoDict = {}
            infoDict['scenicId'] = id
            infoDict['guide_num'] = len_note_list
            infoDict['note_num'] = len_guide_list
            infoDict['answer_num'] = len_answer_list
            infoDict['crawlTime'] = now_time
            infoDict['scenic_name'] = name
            infoDict['sitefrom'] = "马蜂窝"
            return infoDict
        except Exception as e:
            print(e)

    # def writeData(traininfoList):
    #
    #     with open('xiecheng.csv','w',newline='') as fs:
    #
    #         writer = csv.DictWriter(fs,fieldnames=['出发时间','出发车站','需要耗时','车次信息','到达时间','到达车站','车票价格','剩余车票'])
    #
    #         writer.writeheader()
    #         writer.writerows(traininfoList)

    def getScenic(self):
        sql1 = "select id,name from scenics where id > 53"
        sql2 = 'INSERT INTO scenic_index(scenicId,hot_guide_num,elite_guide_num,guide_num,note_num,answer_num,crawlTime,scenic_name,sitefrom) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        # insert(sql, (2, 'wang', 13))
        conn = pymysql.connect(host='202.193.53.151', port=3306, user='root', passwd='root', db='travel')
        cur = conn.cursor()
        cur.execute(sql1, None)
        results = cur.fetchall()
        i=0
        for row in results:
            i=i+1
            pageLink = xiechengUrl.format(str(row[1]).replace(" ", ""))
            source = self.getSource(pageLink)
            dict = self.getEveryItem(row[0], row[1], source)
            # print(dict['scenicId'])
            # sql2.format(dict['scenicId'],dict['guide_num'],dict['note_num'],dict['answer_num'],dict['crawlTime'],dict['sitefrom'])
            args = [dict['scenicId'], 0, 0, dict['guide_num'], dict['note_num'], dict['answer_num'], dict['crawlTime'],
                    dict['scenic_name'], dict['sitefrom']]
            print(args)
            if i % 5 == 0 :
                time.sleep(5)
            cur.execute(sql2,
                        args)
            conn.commit()
        cur.close()
        conn.close()

if __name__ == '__main__':
    getScenic()







