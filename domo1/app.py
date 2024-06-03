from flask import Flask, render_template, request, redirect
import pymysql

# 实例化Flask类
app = Flask(__name__)

# 创造一个全局列表来储存可以被选择的运动，创造一个字典来储存名字和运动的关系
sports = ["basketball", "football", "ping pong"]
register = {}

# 创建一个路由，用来渲染注册页面。把可以选择的运动作为参数传入
@app.route("/index", methods=(["GET"]))
def index():
    return render_template("index.html", sports=sports)

# 创建一个路由，用来接收用户的表单数据，并测试用户是否输入正确
@app.route("/greet", methods=(["POST"]))
# methods=(["POST"])，为接收用户数据的声明
def greet():
    if request.method == "POST":
        name = request.form.get("name")
        sport = request.form.get("sports")
        # 检测试名字和运动是否符合需求，并传入错误信息到HTML页面中
        if name == "":
            warn = "您没有输入名字"
            return render_template("failure.html",warn=warn)
        if sport not in sports:
            warn = "您选择的运动，不在可选的运动中"
            return render_template("failure.html", warn=warn)
        else:
            # 把用户的的名字和运动添加到字典register中
            register[name] = sport

            # 把用户的名字和运动信息添加到数据库中
            db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
            cursor = db.cursor()
            cursor.execute("use test")
            cursor.execute("select * from sports;")
            cursor.execute(f"INSERT INTO sports(name, sport) VALUES('{name}', '{sport}');")
            # 关闭事务
            db.commit()
            # 关闭连接
            db.close()

            return render_template("greet.html", name=name, sport=sport)

# 创建一个路由，用来储存用户提交的数据
@app.route ("/Register", methods=(["GET", "POST"]))
def Register():

    # 先判断用户是否点击删除按钮，用自动增长的id来交换信息
    value = request.form.get("id")
    print(value)
    # 如果用户点击删除，那就在数据库中将信息删除
    if value != None:
        db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
        cursor = db.cursor()
        cursor.execute("use test")
        cursor.execute(f"delete from sports where id = {value};")
        db.commit()
        db.close()
        redirect("Register")
    # 从数据库列表中获取用户注册信息
    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
    cursor = db.cursor()
    cursor.execute("use test")
    cursor.execute("select * from sports;")
    data = cursor.fetchall()
    db.commit()
    db.close()

    return render_template("Register.html", register=register, data=data)


app.run(debug=True)
