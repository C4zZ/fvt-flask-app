import configparser
import os


class DBConfigReader:
    """ reads host, user, password and db values from specified config file on database instantiation.
    """
    def __init__(self, config_filename):

        # getting path where this module (DBConfigReader.py) is located adn appending
        # configs dir
        filedir = os.path.dirname(os.path.realpath(__file__)) + "\\configs\\"


        with open(filedir + config_filename, "r") as f:
            self.configParser = configparser.ConfigParser()
            self.configParser.read_file(f)

    def getHost(self):
        return self.configParser["Main"]["HOST"]

    def getUser(self):
        return self.configParser["Main"]["USER"]

    def getPassword(self):
        return self.configParser["Main"]["PASSWORD"]

    def getDB(self):
        return self.configParser["Main"]["DB"]
