from flask import Flask, render_template ,request
from flask import render_template
import json
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
	 

@app.route("/index")
def index():
	name="labib hasan"
	return render_template("labib.html", name2= name)
app.run(debug=True)