import configparser


class DBConfigReader:
    """ reads host, user, password and db values from specified config file on database instantiation.
    """
    def __init__(self, config_filename):
        with open("configs\\" + config_filename) as f:
        self.configParser = configparser.ConfigParser()
        self.configParser.read_file(f)

    def getHost(self):
        return self.configParser["HOST"]

    def getUser(self):
        return self.configParser["USER"]

    def getPassword(self):
        return self.configParser["PASSWORD"]

    def getDB(self):
        return self.configParser["DB"]
