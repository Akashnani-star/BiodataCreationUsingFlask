from flask import Flask,render_template,request,redirect,url_for
from flask import jsonify
import os

picFolder = os.path.join("static","pics")

app=Flask(__name__)

app.config["UPLOAD_FOLDER"]=picFolder

@app.route("/",methods=["POST","GET"])
def home_page():
	if request.method == "GET":
		return render_template("formf.html")
	else:
		username = request.form.get("username")
		fathername = request.form.get("fathername")
		mothername = request.form.get("mothername")
		dob = request.form.get("dob")
		email = request.form.get("email")
		image = request.files["fi"]
		image.save("./static/pics/"+image.filename)
		imagename = image.filename
		height = request.form.get("height")
		qual = request.form.get("qual")
		address = request.form.get("address")
		pic1Dp = os.path.join(app.config["UPLOAD_FOLDER"],imagename)
		pic2Ticks = os.path.join(app.config["UPLOAD_FOLDER"],"ticks.png")
		pic3Bg = os.path.join(app.config["UPLOAD_FOLDER"],"d.jpg")
		jsonstr ={"username":username,"fathername":fathername,"mothername":mothername,"dob":dob,"email":email,"imagename":imagename,"height":height,"qualification":qual,"address":address}
		return render_template("index1.html",jsonstr=jsonstr,dp=pic1Dp,ticks=pic2Ticks,bg=pic3Bg)
		
app.run(host="0.0.0.0",port=5000)
