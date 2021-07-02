from flask import Flask, render_template ,request
from flask import render_template
import json
from bs4 import BeautifulSoup as b
import re
import requests

url="https://salah.com/"
url2="https://dateandtime.info/citysunrisesunset.php?id=1185241"

html= requests.get(url)
html2=requests.get(url2)

soup= b(html.text,'html.parser')
soup2=b(html2.text,'html.parser')

soup.prettify()
soup2.prettify()

j=soup.select("dd,dt")
j2=soup2.select(".short12hm")

li = list(map(lambda x: x.text ,j))

k=[]
for i in range(len(li)) :
		 	if i%2!=0:
		 		k.append((li[i].strip("\n").strip(" ")+"\n"))
		 	else:
		 		k.append((li[i].strip("\n").strip(" ")+" "))
k.insert(8,"Sunset "+j2[1].text.replace(" ","")+"\n")


app= Flask(__name__)

	
	
	
	


@app.route("/")
def main():
	 	print("hi")
	 	if type(request.args.get("d")) is str:
	 		d= json.loads(request.args.get("d"))
	 		f=open("./player_scores.txt","a")
	 		f.write(f"{d['name']} {d['score']}\n")
	 		print(d['name'])
	 	
	 	return render_template("game.html")


@app.route("/index")
def index():
	name=soup.text
	
	return "".join(k)



if __name__ == "__main__": 

        app.run() 


