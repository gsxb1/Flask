from flask import Flask, render_template, request, redirect, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 设置会话密钥
app.permanent_session_lifetime = timedelta(minutes=30)  # 设置会话过期时间为 30 分钟
name = ""
# index为主页面，展示系统拥有的商品
@app.route("/index", methods=["GET", "POST"])
def index():
    print(name)
    if session != None:
        # name = session["username"]
        return render_template("index.html", name=session)
    else:
        return redirect("/login")

# 用户的登录页面
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # 假设用户登录成功，获取用户名并存储到会话中
        name = request.form.get("name")
        password = request.form.get("password")
        session[name] = password
        return redirect("/index"), name
    else:
        return render_template("login.html")

@app.route("/logout", methods=["POST"])
def logout():
    logout = request.form.get("logout")
    del session[logout]
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
