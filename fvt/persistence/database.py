import pymysql as PyMySQLdb

from fvt.DBConfigReader import DBConfigReader

conn = PyMySQLdb.connect('localhost', 'schema', '3iRLJcC40xkyI8JIZTpv', 'fvt')
database = conn.cursor(PyMySQLdb.cursors.Cursor)


class PyMySQLDBConnection(object):
    """
    database class for fvt-flask-app with custom methods vor accessing needed verbs and track the input of the user
    """
    def __init__(self, config_filename="defaultDB.cfg"):

        self.connection = None
        self.cursor = None

        configReader = DBConfigReader(config_filename)

        self.host = configReader.getHost()
        self.user = configReader.getUser()
        self.password = configReader.getPassword()
        self.db = configReader.getDB()

    def __enter__(self):
        self.connection = PyMySQLdb.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        self.cursor.close()


def trackUserPerformance(verbform, verbsolution, erroneousUserInput, isVerbCorrect, date):
    with PyMySQLDBConnection().connection.cursor() as cursor:

        cursor.execute("INSERT INTO trackusersuccessfailure (verbform, verb, erroneousUserInput, state, date) VALUES "
                     "(%s, %s, %s, %s, %s)", (verbform, verbsolution, erroneousUserInput, isVerbCorrect, date))
        conn.commit()

    # TODO: write custom database methods for database access features inside the actual app


def getColumnNamesFromTable_trackusersuccessfailure():

    with PyMySQLDBConnection() as db:
        cursor = db.cursor

        cursor.execute("desc trackusersuccessfailure")

        field_names = [column[0] for column in cursor.fetchall()]

        return field_names
