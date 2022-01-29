import os


class Config:
    TESTING = False
    ENV_VAR = os.environ.get("ENV_VAR")
    FLASK_ENV = os.environ.get("FLASK_ENV")
    BING = os.environ.get("BING")


    MAIL_SERVER = 'localhost'
    MAIL_PORT = 1025
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = '' # os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = '' # os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = 'ma@mail.com' # os.environ.get("MAIL_DEFAULT_SENDER")


class ProductionConfig(Config):
    FAV_FLOWER = "rose"


class DevelopmentConfig(Config):
    FAV_FLOWER = "sunflower"


class TestingConfig(Config):
    FAV_FLOWER = "moonlight petal"
    TESTING = True
