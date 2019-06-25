import configparser


class DBConfigReader:
    """ reads host, user, password and db values from specified config file on database instantiation.
    """
    def __init__(self, config_filename):
        self.configParser = configparser.ConfigParser()
        self.configParser.read("configs\\" + config_filename)

    def getHost(self):
        pass
        # return self.configParser["HOST"]

    def getUser(self):
        pass

    def getPassword(self):
        pass

    def getDB(self):
        pass
