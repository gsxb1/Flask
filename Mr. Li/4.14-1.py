from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField,EmailField
from wtforms.validators import DataRequired,Length,EqualTo,NumberRange,Email
app = Flask(__name__)
class jk(FlaskForm):
    usename = StringField(label='姓名：',render_kw={'required':False},
                          validators=[DataRequired(message='用户名不能为空'),
                          Length(2,5,message='长度应该为2~5个字符')])
    nianlin = IntegerField('年龄：',render_kw={'required':False},
                          validators=[DataRequired(message='年龄不能为空'),
                          NumberRange(18,25,message='应为有效范围18~25')])
    banji = IntegerField('班级：', render_kw={'required': False},
                           validators=[DataRequired(message='班级不能为空'),
                           NumberRange(1, 6, message='应为有效范围1~6')])
    lianxi = EmailField('联系邮箱：', render_kw={'required': False},
                           validators=[DataRequired(message='联系邮箱不能为空')])
    password = PasswordField('密码：',render_kw={'required':False},
                             validators=[DataRequired(message='密码不能为空')])
    password2 = PasswordField('再次确认密码：',render_kw={'required':False},
                              validators=[DataRequired(message='密码不能为空'),
                               EqualTo('password',message='两次密码不一致')])
    submit = SubmitField('注册')

app.config['SECRET_KEY'] = 'your_secret_key'
@app.route('/',methods = ['GET','POST'])
def ui():
    frome = jk()
    if frome.validate_on_submit():
        return '注册成功！'
    return render_template('4.14-1.html',frome=frome)
if __name__ == "__main__":
    app.run()