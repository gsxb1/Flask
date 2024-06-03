from flask import Flask, render_template

app = Flask(__name__)


@app.route('/text')
def hello_world():
    a = [1, 2, 3]
    b = {"姓名": "帅马"}
    return render_template("html.html", a = a, b = b)

@app.route('/control')
def control():
    a = 18
    book = [{"name":"活着"},{"name":"许三观卖血记"}]
    return render_template("control.html", a = a, book = book)

@app.route('/son')
def son():
    return render_template("son.html")


if __name__ == '__main__':
    app.run()

