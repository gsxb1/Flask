from flask import Flask, render_template, request, redirect, session
from datetime import timedelta
import pymysql
from test import Database
import ast

database = Database()
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 设置会话密钥
app.permanent_session_lifetime = timedelta(minutes=30)  # 设置会话过期时间为 30 分钟
books = [
        ["余华", "活着"],
        ["余华", "许三观卖血记"],
        ["莫言", "生死疲劳"],
        ["莫言", "丰乳肥臀"],
        ["鲁迅", "呐喊"],
        ]

# index为主页面，展示拥有的商品
@app.route("/", methods=["GET", "POST"])
def index():
    data = database.query(1, 0)
    try:
        if [True for i in data if session["name"] in i]:
            # 遍历names列表，如果有名字在session中，那就进入到首页
            # 如果session中没有names中的名字，那就又跳转到登录页
            # print(session["name"])
            return render_template("index.html", books=books)
        else:
            return render_template("login.html")
    except:
        return render_template("login.html")




# 用户的登录页面
@app.route("/login", methods=["GET", "POST"])
def login():
    # 如果没有数据传递过来，那就跳转到登录页
    # 如果有用户的数据传过来，那就将他的名字作为值给到session["name"]
    # 将用户名以及密码保存在login，创建以用户名为表明的购物车表
    if request.method == "POST":
        data = database.query(0, "login")
        name = request.form.get("name")
        for i in data:
            if i == name:
                error = "你的用户名已经存在了"
                return render_template("login.html")
        # 假设用户登录成功，将获取的用户名存储到会话中
        name = request.form.get("name")
        password = request.form.get("password")
        session["name"] = name
        database.login(name, password)
        database.Add_Data_Table(name)
        return redirect("/")
    else:
        return render_template("login.html")

# 注销/删除用户数据
@app.route("/logout")
def logout():
    pass

# shopping_cart（购物车）页面
# 获取首页传来的book信息，存入数据表中
# 再从表中拿到购物车数据，传入shopping_cart.html中
@app.route("/shopping_cart", methods=["GET", "POST"])
def shopping_cart():
    try:
        book = request.form.getlist("book")
        # 把都拿到的book转换为列表
        book_list = ast.literal_eval(book[0])
        # 将的到的购物加入数据库
        database.insert_data(session["name"], book_list[1], book_list[0])
        return redirect("/")
    except:
        if request.form.getlist("book") == []:
            data = database.query(0, session["name"])
            return render_template("shopping_cart.html", book=data)
        return render_template("login.html")

@app.route("/del_shopping_cart", methods=["GET", "POST"])
def del_shopping_cart():
    try:
    # 获取需要删除的书名
        del_book = request.form.getlist("del_book")
        database.Delete_data(session["name"], del_book[0])
        # 获取现在的数据库的内容
        data = database.query(0, session["name"])
        return render_template("shopping_cart.html", book=data)
    except:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)