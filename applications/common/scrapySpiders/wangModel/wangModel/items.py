# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 途牛的景点信息和评价
class WangmodelItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field() #景点id
    name = scrapy.Field() #景点名称
    begin_price = scrapy.Field() #起步价
    satisfy_present = scrapy.Field()  #满意度
    remarkAmount = scrapy.Field()  #评价总数
    compGrade3Amount = scrapy.Field()  #评价满意的人数
    compGrade2Amount = scrapy.Field()  #评价一般的人数
    compGrade1Amount = scrapy.Field()  #评价不满意的人数
    img = scrapy.Field() #景点图片封面
    address = scrapy.Field() #景点地址
    time_arrange = scrapy.Field() #开放时间等
    commentlist = scrapy.Field() #评论

#途牛酒店信息和酒店评价
class TuniuhotelItem(scrapy.Item):
    id=scrapy.Field()
    hname=scrapy.Field()
    starname=scrapy.Field()
    hpic=scrapy.Field()
    haddress=scrapy.Field()
    business=scrapy.Field()
    distance=scrapy.Field()
    hlowstprice=scrapy.Field()
    hcomments=scrapy.Field()
    others=scrapy.Field()

class HornetNestNoteItem(scrapy.Item):
    id = scrapy.Field()
    url=scrapy.Field()
    title = scrapy.Field()
    total=scrapy.Field()
    see=scrapy.Field()
    collect=scrapy.Field()
    commentNum=scrapy.Field()

class WeiboItem(scrapy.Item):
    id=scrapy.Field()
    userid=scrapy.Field()
    screen_name=scrapy.Field()
    fins=scrapy.Field()
    artilelist=scrapy.Field()
    total_artiles=scrapy.Field()


class TongchenTrainItem(scrapy.Item):
    id = scrapy.Field()  #id
    site = scrapy.Field()  #id
    place_from = scrapy.Field()
    place_to = scrapy.Field()
    date = scrapy.Field()
    total_count = scrapy.Field()
    from_station=scrapy.Field()
    to_station=scrapy.Field()
    from_time=scrapy.Field()
    to_time=scrapy.Field()
    seat_name=scrapy.Field()
    seat_price=scrapy.Field()
    seats_left=scrapy.Field()
    type=scrapy.Field()
    status=scrapy.Field()

