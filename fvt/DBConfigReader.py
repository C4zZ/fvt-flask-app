import configparser


class DBConfigReader:
    """ reads host, user, password and db values from specified config file on database instantiation.
    """
    def __init__(self, config_filename):
        self.configParser = configparser.ConfigParser()
        self.configParser.read("configs\\" + config_filename)

    def getHost(self):
        return self.configParser["HOST"]

    def getUser(self):
        return self.configParser["USER"]

    def getPassword(self):
        return self.configParser["PASSWORD"]

    def getDB(self):
        return self.configParser["DB"]
