class Config(object):
    """ Common configurations across all environments """

class DevConfig(Config):
    """ Dev Environment configuration """
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProdConfig(Config):
    """ Prod Environment configuration """
    DEBUG = False

app_config = {
    'dev': DevConfig,
    'prod': ProdConfig }
