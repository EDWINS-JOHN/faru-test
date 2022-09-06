import configparser

config=configparser.RawConfigParser()


config.read("../Configurations/config.ini") 


class ReadConfig:
    @staticmethod
    def getAppURL():
        url=config.get('re-usable','baseurl')
        return url

    @staticmethod
    def get_email():
        email=config.get('re-usable','email')
        return email

    @staticmethod
    def get_password():
        password=config.get('re-usable','password')
        return password

