from flask import Flask, render_template
app = Flask(__name__)

def new(str):
    str = str.strip(' ')
    str = str.strip('=')
    str = str.strip('+')
    str = str.replace('hello','')
    return str
app.add_template_filter(new,"new")

def abc(str):
    str = str[::-1]
    return str
app.add_template_filter(abc,"abc")

@app.route('/')
def _():
    num = -12.6
    new_list = [4, 4, 2, 1, 7, 6, 5]
    str = "   hello you hello are hello good!   "
    return render_template("_.html", num = num, new_list = new_list, str = str)

if __name__=="__main__":
    app.run(debug=True)






