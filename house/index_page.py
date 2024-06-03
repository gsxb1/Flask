from flask import Blueprint, render_template
from models import House

# 创建蓝图
index_page = Blueprint('index_page',__name__)

@index_page.route('/')
def index():
    # 获取房源总数
    house_total_num = House.query.count()
    # 获取6条新发布的房源
    house_new_list = House.query.order_by(House.publish_time.desc()).limit(6).all()
    # 获取4条浏览量最高的房源
    house_hot_list = House.query.order_by(House.page_views.desc()).limit(4).all()
    return render_template('index.html',num=house_total_num,house_new_list=house_new_list,house_hot_list=house_hot_list)