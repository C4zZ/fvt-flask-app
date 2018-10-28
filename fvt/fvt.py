from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from . db import conn, db
from . collect import URLrequesttoString
from . helpers import newRandomVerb, checkVerb
from .verbtraininghelper import createFile, experiment
import random

# fvt database
#
# schema
# 3iRLJcC40xkyI8JIZTpv

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    experiment()
    return render_template("index.html", verb = "")


@app.route("/collect", methods=["POST", "GET"])
def collect():
    if request.method == "POST":
        # if a url was submitted, get its html as a String
        if request.form.get("url"):
            url = request.form.get("url")
            pagestring = URLrequesttoString(url)

            return(pagestring)
        # else do this
        else:
            return "NO URL WAS GIVEN TO CLIENT!"
        
        return str(requestdict)
        

        
    else:
        return render_template("collect.html")

@app.route("/newverb", methods=["GET"])
def newverb():
    newverb = newRandomVerb()
    return newverb

@app.route("/validateverb", methods=["POST"])
def validateverb():
    answer = request.form.get("verbform")
    userinput = request.form.get("userverb")
    isverb = checkVerb(userinput, answer)
    return isverb