from flask import Flask, request, render_template, g

from fvt.AppConfigReader import AppConfigReader
from fvt.persistence.database import PyMySQLDBConnection
from .collect import URLrequesttoString
from .helpers import getNewVerb, isUserInputCorrect

""" 
__init__.py contains mostly application factory methods. For now mainly
the create_app() method
"""


def create_app(config_filename="productionApp.cfg"):
    """
    create_app instantiates a Flask object for the fvt project with all of its endpoints
    """
    app = Flask(__name__, instance_relative_config=False)

    configReader = AppConfigReader(config_filename)

    app.testing = configReader.isTesting()
    app.debug = configReader.isDebug()

    @app.before_request
    def init_database():
        if app.testing:
            # here a database object with parameters for testing purposes is initialized.
            g.db = PyMySQLDBConnection("testingDB.cfg")
        else:
            # here a database object gets initialized with the default config 'production.cfg' meaning a database object
            # for a production environment.
            g.db = PyMySQLDBConnection()

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
