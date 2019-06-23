from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from .database import conn, db
from .collect import URLrequesttoString
from .helpers import getNewVerb, isUserInputCorrect

# fvt database
#
# schema
# 3iRLJcC40xkyI8JIZTpv

""" __init__.py contains mostly application factory methods. For now mainly
    the create_app() method
"""


def create_app(config_filename=None):
    """ create_app instantiates a Flask object for the fvt project with all of its endpoints
    """
    app = Flask(__name__, instance_relative_config=False)

    # creating database
    db =

    if config_filename:
        config_file_path = "configs\\" + config_filename
        app.config.from_pyfile(config_file_path)

    # initialize_extensions(app)
    # register_blueprints(app)

    @app.route("/")
    def index():
        return render_template("index.html", verb="")

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
    def generateNewVerb():
        return getNewVerb()

    @app.route("/validateverb", methods=["POST"])
    def validateverb():

        correctVerbform = request.form.get("verbform")
        userInput = request.form.get("userverb")
        return isUserInputCorrect(userInput, correctVerbform)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=5000)
