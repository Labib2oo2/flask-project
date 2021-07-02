from flask import Flask, render_template ,request
from flask import render_template
import json
from bs4 import BeautifulSoup as b
import re
import requests

url="https://salah.com/"

html= requests.get(url)

soup= b(html.text,'html.parser')
soup.prettify()
app = Flask(__name__)

	
	
	
	


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
	
	return name


if __name__ == "__main__": 

        app.run() 

