import pymysql as PyMySQLdb

conn = PyMySQLdb.connect('localhost', 'schema', '3iRLJcC40xkyI8JIZTpv', 'fvt')
database = conn.cursor(PyMySQLdb.cursors.Cursor)

# TODO: Doc comments

class FVT_DB:

    def __init__(self, config_filename="defaultDB.cfg"):

        self.host = "localhost"
        self.user = "schema"
        self.password = "3iRLJcC40xkyI8JIZTpv"
        self.db = "fvt"

        conn = PyMySQLdb.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        database = conn.cursor(PyMySQLdb.cursors.Cursor)

    def close(self):
        return
# TODO: database.connect() should get its parameters form a config file that doesnt get pushed to remote repo
# TODO: write custom database methods for database access features inside the actual app
