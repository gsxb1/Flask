#导入Flask类
from flask import Flask
#实例化Flask类
app = Flask(__name__)
#定义视图函数，并为该函数注册路由
@app.route("/")
def hello_flask():
    return "<p>Hello, Flask!</p >"
#启动开发服务器
app.run()