from flask import Flask, render_template ,request
from flask import render_template
import json
import requests
app = Flask(__name__)

	
	
	
	


@app.route("/")
def js():
	 	if (request.args.get("d")==True):
	 		d= json.loads(request.args.get("d"))
	 		f=open("player_scores.txt","a")
	 		f.write(f"{d['name']} {d['score']}\n")
	 		return render_template("game.html")
	 	else:
	 		return render_template("game.html")
@app.route("/rqst")
def rqst():
	link=request.args.get("link")
	html2=requests.get(link)
	print(html2.text)
	return html2.text
	
@app.route("/news")
def news():
	
	return render_template("todaynews.html")

	 
import pymongo 
import urllib
@app.route("/mon")
def mon():
	client = pymongo.MongoClient("mongodb://Labib:"+urllib.parse.quote_plus("949802loveeve:>")+"@test-shard-00-00.y1zlb.mongodb.net:27017,test-shard-00-01.y1zlb.mongodb.net:27017,test-shard-00-02.y1zlb.mongodb.net:27017/test?ssl=true&replicaSet=atlas-a4yw33-shard-0&authSource=admin&retryWrites=true&w=majority")
	db=client.honululu
	posts=db.labib
	posts.insert_one({"name":"labib"})
	return "mongo db"



if __name__ == "__main__": 

        app.run() 
