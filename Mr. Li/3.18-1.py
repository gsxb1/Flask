from flask import Flask, session, request, url_for, redirect

app = Flask(__name__)
app.secret_key = '123456'
@app.route('/home')
def home():
    if 'username' in session:
        return f'你好:{session.get("username")}欢迎来到此次页面'
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect(url_for('home'))
    return '''
              <form method="post">
                <p>用户名:<input type=text name=username></p >
                <p>密  码:<input type=password name=password></p >
                <p><input type=submit value='登录'>
              </form>
        '''
if __name__ == '__main__':
    app.run()

