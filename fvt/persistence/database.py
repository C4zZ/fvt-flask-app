import pymysql as PyMySQLdb

from fvt.DBConfigReader import DBConfigReader

conn = PyMySQLdb.connect('localhost', 'schema', '3iRLJcC40xkyI8JIZTpv', 'fvt')
database = conn.cursor(PyMySQLdb.cursors.Cursor)


class PyMySQLDBConnection(object):
    """
    database class for fvt-flask-app with custom methods for accessing needed verbs and track the input of the user.
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
        method for creating connection for current database instance before 'with' statement.
        """

        self.connection = PyMySQLdb.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        method for closing connection for current database instance after 'with' statement.
        """
        self.connection.close()

    def getColumnNamesFromTable(self, table_name):
        """
        getColumnNames requests all column names via below query,formats all column names as a list and returns this list.
        :param table_name: the name of the table form which all column names should be fetched.
        :return: list of all column names form table with table_name.
        """

        with self as db:
            cursor = db.connection.cursor()

            # be wary of sql injection here?
            query = "desc %s" % table_name

            cursor.execute(query)

            field_names = [column[0] for column in cursor.fetchall()]

            return field_names

    def getTableNames(self):
        """
        getTableNames request all available table names form current database, puts all table names into a list and
        returns it.
        """

        with self as db:
            cursor = db.connection.cursor()

            cursor.execute(
                "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = %s",
                (db.db))

            table_names_list = [element[0] for element in cursor.fetchall()]

            return table_names_list

    def trackUserPerformance(self, verbform, verbsolution, erroneousUserInput, isVerbCorrect, date):
        """
        trackUserPerformance tracks whether the user typed in the correct verb or not. It documents the users input when
        it was wrong and when this input was typed in.
        :param verbform: the string containing person, number, tense and baseVerb which are important for the user to type
        in the correct answer e.g. the grammatical form of the actual verb which the user needs to type in.
        :param verbsolution: the correct verb build from the verbform. Needs to be documented for if the user types in
        a wrong verb.
        :param erroneousUserInput: the wrong input of the user if any
        :param isVerbCorrect: 0 for the information that the user input was correct and 1 for the information that the
        user input was incorrect.
        :param date: the date when the user input happened in the format dd-mm-yyyy.
        """

        with self as db:
            cursor = db.connection.cursor()

            cursor.execute(
                "INSERT INTO trackusersuccessfailure (verbform, verb, erroneousUserInput, state, date) VALUES "
                "(%s, %s, %s, %s, %s)", (verbform, verbsolution, erroneousUserInput, isVerbCorrect, date))

            conn.commit()