import pymysql as PyMySQLdb

from fvt.DBConfigReader import DBConfigReader

conn = PyMySQLdb.connect('localhost', 'schema', '3iRLJcC40xkyI8JIZTpv', 'fvt')
database = conn.cursor(PyMySQLdb.cursors.Cursor)


class FVT_DB:
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

        self.connect()

    def connect(self):
        """
        open database connection.
        """
        self.connection = PyMySQLdb.connect(host=self.host, user=self.user, password=self.password, db=self.db)

    def disconnect(self):
        return


def trackUserPerformance(verbform, verbsolution, erroneousUserInput, isVerbCorrect, date):
    with FVT_DB().connection.cursor() as cursor:

        cursor.execute("INSERT INTO trackusersuccessfailure (verbform, verb, erroneousUserInput, state, date) VALUES "
                     "(%s, %s, %s, %s, %s)", (verbform, verbsolution, erroneousUserInput, isVerbCorrect, date))
        conn.commit()

    # TODO: write custom database methods for database access features inside the actual app
