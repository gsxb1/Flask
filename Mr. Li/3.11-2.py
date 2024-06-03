from flask import Flask,after_this_request
app = Flask(__name__)

with app.app_context():
    print('这是第一次请求前会执行的函数')
# @app.before_first_request
# def b_f_r():
#     print('这是第一次请求前会执行的函数')

@app.before_request
def b_r():
    print('这是每次请求之前都会执行的函数')

@app.route('/')
def index():
    print('hello')
    @after_this_request
    def a_t_r(response):
        print('这是这个请求之后可以执行的函数')
        return response   #将响应信息返回
    return 'hello flask'  #在页面中返回响应信息

@app.after_request
def a_r(response):
    print('这是程序没有异常是每次请求后执行的函数')
    return response

@app.teardown_request
def t_r(error):
    print('这是程序即使有异常时每次请求之后也会执行的函数')

if __name__ == '__main__':
    app.run()