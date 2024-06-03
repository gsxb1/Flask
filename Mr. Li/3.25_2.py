from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def flask():
    return render_template("3.25_2.html")

app.run()
