import pymysql as MySQLdb
from .db import conn, db

# turn SELECT output to a dictionary with the respective column names
# of a table as key values
db = conn.cursor(MySQLdb.cursors.DictCursor)

# présent
def buildprésent(inf, pz):
    db.execute("SELECT * FROM présent WHERE infinitiv = %s", (inf,))
    verbrow = db.fetchone()
    verbsolution = verbrow[pz]
    return verbsolution

# passé-composé 
def buildpc(inf, pz):

    db.execute("SELECT vom FROM présent WHERE infinitiv = %s", (inf,))
    vom = db.fetchone()["vom"]
    # if current verb is a verb of motion (vom) in passé composé
    # then we need to use the participe passé of être as the auxiliaryverb
    result = ""
    db.execute("SELECT pp FROM présent WHERE infinitiv = %s", (inf,))
    pp = db.fetchone()["pp"]
    
    if vom == "1":
        db.execute("SELECT * FROM présent WHERE infinitiv = 'être'")
        auxiliary = db.fetchone()[pz]
        result = auxiliary
    else:
        db.execute("SELECT * FROM présent WHERE infinitiv = 'avoir'")
        auxiliary = db.fetchone()[pz]
        result = auxiliary

    return result + " " + pp
    

