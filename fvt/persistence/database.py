import pymysql as PyMySQLdb

conn = PyMySQLdb.connect('localhost', 'schema', '3iRLJcC40xkyI8JIZTpv', 'fvt')
db = conn.cursor(PyMySQLdb.cursors.Cursor)

class FVT_DB:

    def __init__(self):

        conn = PyMySQLdb.connect('localhost', 'schema', '3iRLJcC40xkyI8JIZTpv', 'fvt')
        db = conn.cursor(PyMySQLdb.cursors.Cursor)

# TODO: save database connection to flask g variable
# TODO: database.connect() should get its parameters form a config file that doesnt get pushed to remote repo
# TODO: write custom database methods for database access features inside the actual app
