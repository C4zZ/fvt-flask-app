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
                self.configParser = configparser.ConfigParser()
                self.configParser.read_file(f)

                # checking if "Main" section exists inside given config file
                self.mainSection = self.configParser._sections["Main"]
            except configparser.MissingSectionHeaderError:
                print("\n\n\nDBConfigReader Error:\n The file {} does not have a \"Main\" section!".format(config_filename))
                raise Exception("the file {} does not have a \"Main\" section!".format(config_filename))

            #TODO: checking if Main section contains the keys "HOST". "USER", "PASSWORD" and "DB"

    def getHost(self):
        return self.mainSection["HOST"]

    def getUser(self):
        return self.mainSection["USER"]

    def getPassword(self):
        return self.mainSection["PASSWORD"]

    def getDB(self):
        return self.mainSection["DB"]
