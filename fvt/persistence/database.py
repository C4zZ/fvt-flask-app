import pymysql as PyMySQLdb

from fvt.DBConfigReader import DBConfigReader

conn = PyMySQLdb.connect('localhost', 'schema', '3iRLJcC40xkyI8JIZTpv', 'fvt')
database = conn.cursor(PyMySQLdb.cursors.Cursor)


class PyMySQLDBConnection(object):
    """
    database class for fvt-flask-app with custom methods for accessing needed verbs and track the input of the user
    """
    def __init__(self, config_filename="defaultDB.cfg"):

        self.connection = None

        configReader = DBConfigReader(config_filename)

        self.host = configReader.getHost()
        self.user = configReader.getUser()
        self.password = configReader.getPassword()
        self.db = configReader.getDB()

    def __enter__(self):
        """
        method for creating connection for current database instance before 'with' statement
        """
        self.connection = PyMySQLdb.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        method for closing connection for current database instance after 'with' statement
        """
        self.connection.close()

    def getColumnNamesFromTable(self, table_name):

        with self as db:
            cursor = db.connection.cursor()
            query = "desc %s" % table_name
            cursor.execute(query)

            field_names = [column[0] for column in cursor.fetchall()]

            d = 9

            return field_names

    def getTableNames(self):
        with self as db:
            cursor = db.connection.cursor()

            cursor.execute(
                "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = %s",
                (db.db))

            table_names_list = [element[0] for element in cursor.fetchall()]

            return table_names_list

    def trackUserPerformance(self, verbform, verbsolution, erroneousUserInput, isVerbCorrect, date):
        with self as db:
            cursor = db.connection.cursor()

            cursor.execute(
                "INSERT INTO trackusersuccessfailure (verbform, verb, erroneousUserInput, state, date) VALUES "
                "(%s, %s, %s, %s, %s)", (verbform, verbsolution, erroneousUserInput, isVerbCorrect, date))

            conn.commit()