import pymysql as PyMySQLdb
from random import randint
from flask import g

from fvt.DBConfigReader import DBConfigReader

conn = PyMySQLdb.connect('localhost', 'schema', '3iRLJcC40xkyI8JIZTpv', 'fvt')
database = conn.cursor(PyMySQLdb.cursors.Cursor)


class PyMySQLDBConnection(object):
    """
    database class for fvt-flask-app with custom methods for accessing needed verbs and track the input of the user.
    """

    def __init__(self, config_filename="productionDB.cfg"):

        self.connection = None

        config_reader = DBConfigReader(config_filename)

        self.host = config_reader.getHost()
        self.user = config_reader.getUser()
        self.password = config_reader.getPassword()
        self.db = config_reader.getDB()
        self.testingDB = config_reader.isTestingDB()

    def __enter__(self):
        """
        method for creating connection for current database instance before 'with' statement.
        """

        self.connection = PyMySQLdb.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        method for closing connection for current database instance after 'with' statement. The connection will only be
        close if the database is not a testing database.
        """
        if not self.testingDB:
            self.connection.close()

    def getColumnNamesFromTable(self, table_name):
        """
        getColumnNames requests all column names via below query, formats all column names as a list and returns this
        list.
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

    def trackUserPerformance(self, verbform, verbsolution, erroneousUserInput, date):
        """
        trackUserPerformance tracks whether the user typed in the correct verb or not. It documents the users input when
        it was wrong and when this input was typed in.
        :param verbform: the string containing person, number, tense and baseVerb which are important for the user to type
        in the correct answer e.g. the grammatical form of the actual verb which the user needs to type in.
        :param verbsolution: the correct verb build from the verbform. Needs to be documented for if the user types in
        a wrong verb.
        :param erroneousUserInput: the wrong input of the user if any
        user input was incorrect.
        :param date: the date when the user input happened with the format dd-mm-yyyy.
        """

        with self as db:
            cursor = db.connection.cursor()

            # 0 get put into the state column for signaling that the user input was incorrect for the given verbform
            if len(erroneousUserInput) > 0:
                cursor.execute(
                    "INSERT INTO trackusersuccessfailure (verbform, verb, erroneousUserInput, state, date) VALUES "
                    "(%s, %s, %s, %s, %s)", (verbform, verbsolution, erroneousUserInput, "0", date)
                )
            # 1 get put into the state column for signaling that the user input was correct for the given verbform
            else:
                cursor.execute(
                    "INSERT INTO trackusersuccessfailure (verbform, verb, erroneousUserInput, state, date) VALUES "
                    "(%s, %s, %s, %s, %s)", (verbform, verbsolution, erroneousUserInput, "1", date)
                )


            # commit query only if this database instance is not for testing purposes
            if not self.testingDB:
                self.connection.commit()

    def getRandomBaseVerb(self):
        """
        getRandomBaseVerb selects all base verbs that exist inside the database, randomly picks one and returns it.
        :return: the randomly picked base verb
        """
        with self as db:
            cursor = db.connection.cursor()

            cursor.execute("SELECT infinitiv FROM présent")
            linkedVerbsList = cursor.fetchall()

            verbsList = []
            for singleElementTuple in linkedVerbsList:
                verbsList.append(singleElementTuple[0])

            verb = verbsList[randint(0, len(verbsList) - 1)]

            return verb

    def build_présent(self, infinitive, person, number):
        """
        build_présent constructs the french tense présent out of the given parameters and returns it.
        :param infinitive: the basic form of a verb, without an inflection binding it to a particular subject or tense
        :param person: person refers to whether the subject is first person (“je” or “nous”), second person (“tu” or “vous”) or third person (“il”/“elle”/“on” or “ils”/“elles”).
        :param number: number refers to whether the subject of the verb is singular or plural.
        :return: the verb constructed with the help of the given parameters in the french présent tense.
        """

        with self as db:
            cursor = db.connection.cursor(PyMySQLdb.cursors.DictCursor)
            column = determine_column(person, number)

            cursor.execute("SELECT * FROM présent WHERE infinitiv = %s", (infinitive,))

            verbrow = cursor.fetchone()
            présent = verbrow[column]

            return présent

    def build_passé_composé(self, infinitive, person, number):
        pass


def callTrackUserPerformance(verbform, verbsolution, erroneousUserInput, date):
    """
    callTrackUserPerformance gets the database from the current application context and calls the database class intern
    method trackUserPerformance(...) with the given parameters.
    :param verbform: the string containing person, number, tense and baseVerb which are important for the user to type
    in the correct answer e.g. the grammatical form of the actual verb which the user needs to type in.
    :param verbsolution: the correct verb build from the verbform. Needs to be documented for if the user types in
    a wrong verb.
    :param erroneousUserInput: the wrong input of the user if any
    user input was incorrect.
    :param date: the date when the user input happened with the format dd-mm-yyyy.
    """
    db = get_db()
    db.trackUserPerformance(verbform, verbsolution, erroneousUserInput, date)


def callGetRandomBaseVerb():
    """
    callGetRandomBaseVerb gets the database from the current application context and calls the database class intern
    method getRandomBaseVerb(...).
    :return: a random base verb from the database
    """
    db = get_db()
    verb = db.getRandomBaseVerb()
    return verb

def call_build_présent(infinitive, person, number):
    """
    call_build_présent gets the database from the current application context and calls the database class intern
    method call_build_présent(...).
    :param infinitive: the basic form of a verb, without an inflection binding it to a particular subject or tense
    :param person: person refers to whether the subject is first person (“je” or “nous”), second person (“tu” or “vous”) or third person (“il”/“elle”/“on” or “ils”/“elles”).
    :param number: number refers to whether the subject of the verb is singular or plural.
    :return:
    """
    db = get_db()
    présent = db.build_présent(infinitive, person, number)
    return présent


def get_db():
    """
    get_db checks whether or not there is the db key inside the application context variable g. If the key is not
    available then a database connection gets created and saved as value for this key. The value for the db key gets
    returned afterwards.
    """
    if "db" not in g:
        g.db = PyMySQLDBConnection()
    return g.db


def close_db():
    """
    close_db pops the db key form the application context variable g and closes the actual database connection.
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()

def determine_column(person, number):
    return person + number
