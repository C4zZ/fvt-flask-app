import pymysql as PyMySQLdb

conn = PyMySQLdb.connect('localhost', 'schema', '3iRLJcC40xkyI8JIZTpv', 'fvt')
db = conn.cursor(PyMySQLdb.cursors.Cursor)
