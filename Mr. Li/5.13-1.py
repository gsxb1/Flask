from flask import Flask,render_template
from settings import Config,db
from models import House
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
@app.route('/')
def test():
    # return render_template('index.html')
    first_user = House.query.first()
    print(first_user)
    # five_user = House.query.fifth()
    # print(five_user)
    return 'OK'
if __name__ == '__main__':
    app.run(debug=True)