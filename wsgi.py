from flask import Flask, render_template ,request
from flask import render_template
import json
from bs4 import BeautifulSoup as b
import re
import requests

url="https://www.islamicfinder.org/world/bangladesh/1185241/dhaka-prayer-times/#google_vignette"


html= requests.get(url)


soup= b(html.text,'html.parser')

soup.prettify()

j=soup.select(".prayername,.prayertime")

li = list(map(lambda x: x.text ,j))



app= Flask(__name__)

import pymongo 
import urllib
import os
is_prod = os.environ.get('IS_HEROKU', None)

if is_prod:
        Mongo= os.environ.get("MONGODB_URI")
	client = pymongo.MongoClient(Mongo)
	db=client.honululu
	posts=db.labib
else:
	client = pymongo.MongoClient("mongodb://Labib:"+urllib.parse.quote_plus("949802loveeve:>")+"@test-shard-00-00.y1zlb.mongodb.net:27017,test-shard-00-01.y1zlb.mongodb.net:27017,test-shard-00-02.y1zlb.mongodb.net:27017/test?ssl=true&replicaSet=atlas-a4yw33-shard-0&authSource=admin&retryWrites=true&w=majority")
	db=client.honululu
	posts=db.labib	
	


@app.route("/")
def main():
	 
	 	if type(request.args.get("d")) is str:
	 		d= json.loads(request.args.get("d"))
	 		f=open("./player_scores.txt","a")
	 		f.write(f"{d['name']} {d['score']}\n")
	 		
	 	
	 	return render_template("game.html")


@app.route("/index")
def index():
	name=soup.text
	
	return " ".join(li)
	
@app.route("/rqst")
def rqst():
	link=request.args.get("link")
	html2=requests.get(link)
	
	return html2.text
	
@app.route("/news")
def news():
	
	return render_template("todaynews.html")

@app.route("/mon")
def mon():
	posts.insert_one({"name":"labib"})
	return "mongo db"


if __name__ == "__main__": 

        app.run() 


