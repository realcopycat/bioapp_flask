import scrapy

"""
获取内荣没有点赞量收藏量
"""
class WeixinSpider(scrapy.Spider):
    name = 'weixin'
    allowed_domains = ['weixin.qq.com']
    start_urls = ['http://weixin.qq.com/']

    def parse(self, response):
        url="https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin=0&count=5&fakeid=MjM5MTU4MDA3NA==&type=9&query=&token=1865697574&lang=zh_CN&f=json&ajax=1"
        cookie={"ua_id":"M0pQpE2KNnw1HvOXAAAAAE1fDecySy9uYPcTbbxXQRU=",
                "wxuin":"46810516647178",
                "mm_lang":"zh_CN",
                "RK":"79EdPle1Va",
                "ptcz":"f456c97e2c8f1090c61d121feb1eeef1419024051b0ed67a796600b76d0188ce",
                "tvfe_boss_uuid":"6b9a9980f35eae48",
               "pgv_pvid":"5260654758", "o_cookie":"1732095688",
                "sd_userid":"30241653648365907",
                "sd_cookie_crttime":"1653648365907",
                "pgv_pvi":"3187809280",
                "_hjSessionUser_3021617":"eyJpZCI6IjlhOTNkZWFiLTMzMDgtNTE5Yi05NWFlLTY4NGRlNGRjM2RhNSIsImNyZWF0ZWQiOjE2NTgwMjcyNTc1MTIsImV4aXN0aW5nIjpmYWxzZX0=",
                "fqm_pvqid":"6afd8062-36ba-409d-b8b7-5b81ed4b79a6",
                "eas_sid":"t1s6C6I0l577k3v243y953C9j9",
                "Qs_lvt_323937":"1660573260",
                "Qs_pv_323937":"715607012924411500",
                "pgv_info":"ssid=s8054505600",
                "uuid":"290f168055a3887964b014be8c572aeb",
                "rand_info":"CAESIMvL6//JBy3GkYFANvsjpopfu+U1CadTWcrGvE5/iUkg",
                "slave_bizuin":"3865832081", "data_bizuin":"3865832081", "bizuin":"3865832081",
                "data_ticket":"3PNmNqEn/TJReP5OnXXQDWRy8NSPvxdRXgAP1zpmBJEEXd373AHCceq4yOquFumT",
                "slave_sid":"RHZjMFdod1pQdzdHVjEzTUgyZkREeUZYVDR0YUFZUlpreXJYTWZLUDB3TTJIUklGdkhlX213UVVQeFg2cVdtX1FSRDhkcWVTcE5tRm1BZm52R2E2RkpaQkRrbzdoWFpCRWtvVmtZajYydmNMajdwTmpFOUhHWjRYbHlGcGppQ2tBYTc5cmNSVm02RFE1VTNk",
                "slave_user":"gh_0a3b16a337ce",
                "xid":"a1ceb4b8eea06c75fdfd31d65f3767f5",
                "_clck":"3865832081|1|f6k|0"}
        yield scrapy.Request(
            url=url,
            callback=self.parse_item,
            cookies=cookie
        )

    def parse_item(self, response):
        print(response.json())
        data=response.json()
        artilelist=data['app_msg_list']