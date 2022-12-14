
from applications.common.tasks.景区评论标题.scenic_start import Scenic
from applications.common.tasks.线路评论标题.route_start import Route
from applications.common.tasks.酒店评论标题.hotel_title_start import Hotel
from applications.common.tasks.景区攻略.guide_start import Guide


task_list = ['景区评论标题', '线路评论标题', '景区攻略','酒店评论标题']
def 景区评论标题(id, name):
    scenic_start = Scenic()
    scenic_start.run()

def 线路评论标题(id, name):
    scenic_start = Route()
    scenic_start.run()

def 景区攻略(id, name):
    scenic_start = Guide()
    scenic_start.run()

def 酒店评论标题(id, name):
    scenic_start = Hotel()
    scenic_start.run()
