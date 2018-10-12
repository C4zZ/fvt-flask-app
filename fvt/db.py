import pymysql as MySQLdb

conn = MySQLdb.connect('localhost', 'schema', 'DATABASEPASSWORD', 'fvt')
db = conn.cursor(MySQLdb.cursors.Cursor)