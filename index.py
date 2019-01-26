#index.py is necessary for setting this app up on an actual website
import os, sys
sys.path.append("/home/deev/webapps/fvt/htdocs")
sys.path.append("/home/deev/webapps/fvt/htdocs/fvt")

PROJECT_DIR = "/home/deev/webapps/fvt/htdocs/fvt/venv"
activate = os.path.join(PROJECT_DIR, "bin", "activate_this.py")
with open(activate) as f:
    exec(f.read(), {"__file__": activate})
sys.path.append(PROJECT_DIR)

from fvt.fvt import app as application
