from flask import Flask,session,request,url_for
app = Flask(__name__)
@app.route('/kl/jk')
def gr():
    return f"url路径为{url_for('gr'), name }"
if __name__=="__main__":
    app.run()
