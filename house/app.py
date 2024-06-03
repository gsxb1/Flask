from flask import Flask,render_template
from settings import Config,db
from models import House
from index_page import index_page

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(index_page, url_prefix='/')

@app.route('/')
def test():
    # return render_template('index.html')
    first_user = House.query.get(5)
    # print(first_user)
    return f'{first_user}'

if __name__ == '__main__':
    app.run(debug=True)