from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def flask():
    name_list = ["jijia", "rous", "jike"]
    name_dict = {"jijia":"html", "rous":"men", "jike":"ttnk"}
    return render_template("3.25_1.html", name_list = name_list, name_dict=name_dict)

app.run()
