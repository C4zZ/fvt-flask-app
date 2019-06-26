import pymysql as PyMySQLdb

from fvt.DBConfigReader import DBConfigReader

conn = PyMySQLdb.connect('localhost', 'schema', '3iRLJcC40xkyI8JIZTpv', 'fvt')
database = conn.cursor(PyMySQLdb.cursors.Cursor)


class FVT_DB:
    """ database class for fvt-flask-app with custom methods vor accessing needed verbs and track the input of the user
    """
    def __init__(self, config_filename="defaultDB.cfg"):

        configReader = DBConfigReader(config_filename)

        self.host = "localhost"
        self.user = "schema"
        self.password = "3iRLJcC40xkyI8JIZTpv"
        self.db = "fvt"

        """
        self.host = configReader.getHost()
        self.user = configReader.getUser()
        self.password = configReader.getPassword()
        self.db = configReader.getDB()
        """
        conn = PyMySQLdb.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        database = conn.cursor(PyMySQLdb.cursors.Cursor)

    def close(self):
        return
# TODO: database.connect() should get its parameters form a config file that doesnt get pushed to remote repo
# TODO: write custom database methods for database access features inside the actual app
