from flask import Flask, render_template,request,abort
app = Flask(__name__)	
from flask import Flask,render_template,abort
import json
app = Flask(__name__)


@app.route('/',methods=["GET"])
@app.route('/')
def inicio():
	return render_template("inicio.html")
