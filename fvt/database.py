import pymysql as PyMySQLdb

# Todo: reverting the renaming of MySQLdb

conn = PyMySQLdb.connect('localhost', 'schema', '3iRLJcC40xkyI8JIZTpv', 'fvt')
db = conn.cursor(PyMySQLdb.cursors.Cursor)
