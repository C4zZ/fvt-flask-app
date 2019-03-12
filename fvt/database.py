import pymysql as MySQLdb

conn = MySQLdb.connect('localhost', 'schema', '3iRLJcC40xkyI8JIZTpv', 'fvt')
db = conn.cursor(MySQLdb.cursors.Cursor)