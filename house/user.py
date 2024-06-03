from flask import Blueprint, request, Response, jsonify
import json
from models import User
from settings import db

user_page = Blueprint('user_page', __name__)


@user_page.route('/register', methodes=["POST"])  # 注册路由，请求方方法
def register():
    # 获取用户的注册信息，包括用户名、密码、邮箱
    name = request.form['username']
    password = request.form['password']
    email = request.form['email']
    # 查询数据库中是否存在该用户名
    result = User.query.filter(User.name == name).all()
    # 判断用户名是否已经注册，如果没有注册在返回的结果中设置Cookie
    if len(result) == 0:  # 若用户名不存在，说明未注册，则将注册信息保存到数据库中，并在Cookie中设置过期时间
        # 创建User对象
        user = User(name=name, password=password, email=email)
        # 保存数据
        db.session.add(user)
        db.session.commit()  # 提交
        # 构建回应信息
        json_str = json.dumps({'valid': '1', 'msg': user.name})
        res = Response(json_str)  # 实例化的过程中需要给他传入回应内容
        # 将用户信息保存在Cookie中，同时设置时间为2小时
        res.set_cookie('name', user.name, 3600 * 2)
        return res
    # 用户名已经被注册过
    else:
        return jsonify({'valid': '0', 'msg': '用户已注册'})


