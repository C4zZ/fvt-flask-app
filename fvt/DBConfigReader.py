import configparser

# TODO: Doc comments

class DBConfigReader:

    def __init__(self, config_filename):
        self.configParser = configparser.ConfigParser()
        self.configParser.read("configs\\" + config_filename)

    def getHost(self):
        pass
        # return self.configParser["HOST"]

    def getUses(self):
        pass

    def getPassword(self):
        pass

    def getDB(self):
        pass
