import configparser
import os


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
                print("\n\n\nDBConfigReader Error:\n The file {} does not have a \"Main\" section!".format(config_filename))
                raise Exception("the file {} does not have a \"Main\" section!".format(config_filename))

            #TODO: checking if Main section contains the keys "HOST". "USER", "PASSWORD" and "DB"

    def getHost(self):
        return self.mainSection["host"]

    def getUser(self):
        return self.mainSection["user"]

    def getPassword(self):
        return self.mainSection["password"]

    def getDB(self):
        return self.mainSection["db"]
