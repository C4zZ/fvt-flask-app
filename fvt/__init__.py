from flask import Flask

# fvt database
#
# schema
# 3iRLJcC40xkyI8JIZTpv

def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    #initialize_extensions(app)
    #register_blueprints(app)
    return app