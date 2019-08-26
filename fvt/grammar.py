# coding=utf-8
import pymysql as MySQLdb
from fvt.persistence.database import conn

# turn SELECT output to a dictionary with the respective column names
# of a table as key values
db = conn.cursor(MySQLdb.cursors.DictCursor)


# passé-composé 
def buildpc(inf, person, number):
    column = determine_column(person, number)
    db.execute("SELECT vom FROM présent WHERE infinitiv = %s", (inf,))
    vom = db.fetchone()["vom"]
    # if current verb is a verb of motion (vom) in passé composé
    # then we need to use the participe passé of être as the auxiliaryverb
    result = ""
    db.execute("SELECT pp FROM présent WHERE infinitiv = %s", (inf,))
    pp = db.fetchone()["pp"]
    
    if vom == "1":
        db.execute("SELECT * FROM présent WHERE infinitiv = 'être'")
        auxiliary = db.fetchone()[column]
        result = auxiliary
    else:
        db.execute("SELECT * FROM présent WHERE infinitiv = 'avoir'")
        auxiliary = db.fetchone()[column]
        result = auxiliary

    return result + " " + pp


def determine_column(person, number):
    return person + number
