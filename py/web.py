from flask import Flask, render_template,request

from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
	link = "<h1>蔡伃捷Python網頁</h1>"
	link += "<a href=/mis>課程</a><hr>"
	link += "<a href=/today>今天日期</a><hr>"
	link += "<a href=/about>關於伃捷</a><hr>"
	return link

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1><a href=/>"

@app.route("/today")
def today():
    now = datetime.now()
    year = str(now.year)
    month = str(now.month)
    day = str(now.day)
    now = year + "年" + month + "月" + day + "日"

    return render_template("today.html",datetime = now)

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/welcome")
def welcome():
	return render_template("welcome.html",name="蔡伃捷")

@app.route("/welcome", methods=["GET"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")

if __name__=="__main__":
	app.run(debug=True)