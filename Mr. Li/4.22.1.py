from app import app
from app import db
from Model import User
@app.route("/")
def kl():
    name1 = User(username = "李帅龙",email = '163@qq.com')
    name2 = User(username="李四", email='166@qq.com')
    name3 = User(username="王五", email='168@qq.com')
    db.session.add(name1)
    db.session.add_all([name2,name3])
    db.session.commit()
    return 'OK，您成功了'
def ml():
    user = User.query.all()
    print(user)
    user2 = User.query.filter_by(username="李帅龙").first()
    print(user2)
    user3 = User.query.filter_by(email="166@qq.com").first()
    print(user3)
    return 'ok'

if __name__ == '__main__':
    app.run()