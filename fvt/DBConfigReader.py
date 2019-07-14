import configparser
import os
import sys


class DBConfigReader:
    """ reads host, user, password and db values from specified config file on database instantiation.
    """
    def __init__(self, config_filename):

        # getting path where this module (DBConfigReader.py) is located and appending
        # configs dir
        filedir = os.path.dirname(os.path.realpath(__file__)) + "\\configs\\"

        with open(filedir + config_filename, "r") as f:
            try:
                configParser = configparser.ConfigParser()
                configParser.read_file(f)

                # checking if "Main" section exists inside given config file
                self.mainSection = configParser._sections["Main"]
            except configparser.MissingSectionHeaderError:
                print("\nThe file {} does not have a \"Main\" section!".format(config_filename))
                sys.exit(1)

            try:
                self.host = self.mainSection["host"]
                self.user = self.mainSection["user"]
                self.password = self.mainSection["password"]
                self.db = self.mainSection["db"]
                # saving boolean value inside testingDB
                self.testingDB = self.mainSection["testing"] in ("True")
            except KeyError:
                print("\nPlease check whether or not you have the following keys inside the config file: HOST, USER, "
                      "PASSWORD, DB, TESTING")
                sys.exit(1)

    def getHost(self):
        return self.host

    def getUser(self):
        return self.user

    def getPassword(self):
        return self.password

    def getDB(self):
        return self.db

    def isTestingDB(self):
        return self.testingDB