import configparser
import os
import sys


class AppConfigReader:
    """ reads testing and debug values from specified config file on app instantiation.
    """
    def __init__(self, config_filename):

        # getting path where this module (AppConfigReader.py) is located and appending
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
                self.isTesting = self.mainSection["testing"]
                self.isDebug = self.mainSection["debug"]

            except KeyError:
                print("\nPlease check whether or not you have the following keys inside the config file: TESTING, DEBUG")
                sys.exit(1)

    def isTesting(self):
        return self.isTesting

    def isDebug(self):
        return self.isDebug