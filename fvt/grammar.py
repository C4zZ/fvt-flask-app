# coding=utf-8
import pymysql as MySQLdb
from fvt.persistence.database import conn, database

# turn SELECT output to a dictionary with the respective column names
# of a table as key values
db = conn.cursor(MySQLdb.cursors.DictCursor)


# présent
def buildprésent(inf, pz):
    database.execute("SELECT * FROM présent WHERE infinitiv = %s", (inf,))
    verbrow = database.fetchone()
    verbsolution = verbrow[pz]
    return verbsolution


# passé-composé 
def buildpc(inf, pz):

    database.execute("SELECT vom FROM présent WHERE infinitiv = %s", (inf,))
    vom = database.fetchone()["vom"]
    # if current verb is a verb of motion (vom) in passé composé
    # then we need to use the participe passé of être as the auxiliaryverb
    result = ""
    database.execute("SELECT pp FROM présent WHERE infinitiv = %s", (inf,))
    pp = database.fetchone()["pp"]
    
    if vom == "1":
        database.execute("SELECT * FROM présent WHERE infinitiv = 'être'")
        auxiliary = database.fetchone()[pz]
        result = auxiliary
    else:
        database.execute("SELECT * FROM présent WHERE infinitiv = 'avoir'")
        auxiliary = database.fetchone()[pz]
        result = auxiliary

    return result + " " + pp
    

