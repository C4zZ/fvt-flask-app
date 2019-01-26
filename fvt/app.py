from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
#from . db import conn, db
from . collect import URLrequesttoString
from . helpers import newRandomVerb, checkVerb
from .verbtraininghelper import createFile, experiment
from .collect import IMDtodict
import random, json

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

@app.route("/newverb", methods=["POST"])
def newverb():
    #python gets the verbdictionary and creates a new verb from the keys of the dict
    #js on the other hand checks which values (ranging from 0 to 2) are at the end of the verbdictionary
    #if there are no 1 to 3 person in plural and singular the given verbform was completed and can be deleted via js from the dictionary
    return str(type(json.loads(request.form.get("verbDictionary")))) 
    newverb = newRandomVerb()
    return newverb

@app.route("/validateverb", methods=["POST"])
def validateverb():
    answer = request.form.get("verbform")
    userinput = request.form.get("userverb")
    isverb = checkVerb(userinput, answer)
    return isverb