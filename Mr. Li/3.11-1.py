from flask import Flask
from werkzeug.routing import BaseConverter
class a(BaseConverter):
    # regex = "1[3-9]\d{9}$"
    regex = "^[0-9a-zA-Z]*$"
app = Flask(__name__)
# @app.route('/index')
# @app.route('/web')
# def index():
#     return f"<h1>首页</h1?>"
# # app.add_url_rule(rule = '/index' , view_func=index)

app.url_map.converters["mobile"] = a
@app.route('/<mobile:page>')
def page_num(page):
    return f'当前为第{page}页'

if __name__ == '__main__':
    app.run()