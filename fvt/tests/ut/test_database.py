class TestDatabase:
    """
    TestDatabase is responsible for testing database methods reading or writing data form/to the database
    """

    def test_allTablesAvailableInDB(self, testDB):
        """
        testing if all 3 tables (namely 'présent', 'testtbl' and 'trackusersuccessfailure') exist inside the database.
        """
        table_names = testDB.getTableNames()

        assert len(table_names) == 3 and \
            "présent" in table_names and \
            "testtbl" in table_names and \
            "trackusersuccessfailure" in table_names

    def test_getColumnNamesFromTable_trackusersuccessfailure(self, testDB):
        """
        testing if all 6 columns (namely 'error_id', 'verbform', 'verb', 'erroneousUserInput', 'state' and 'date') are
        present inside the table 'trackusersuccessfailure'
        """
        column_names = testDB.getColumnNamesFromTable("trackusersuccessfailure")

        assert len(column_names) == 6 and \
            "error_id" in column_names and \
            "verbform" in column_names and \
            "verb" in column_names and \
            "erroneousUserInput" in column_names and \
            "state" in column_names and \
            "date" in column_names
