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

	
	
	
	


@app.route("/")
def main():
	 
	 	if type(request.args.get("d")) is str:
	 		d= json.loads(request.args.get("d"))
	 		f=open("./player_scores.txt","a")
	 		f.write(f"{d['name']} {d['score']}\n")
	 		print(d['name'])
	 	
	 	return render_template("game.html")


@app.route("/index")
def index():
	name=soup.text
	
	return " ".join(li)



if __name__ == "__main__": 

        app.run() 


