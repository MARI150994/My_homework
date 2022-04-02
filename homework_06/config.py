from os import getenv

SQLALCHEMY_DATABASE_URI = getenv(
    'SQLALCHEMY_DATABASE_URI',
    'postgresql+psycopg2://user:password@localhost/test_flask'
)


class Config:
    DEBUG = False
    TESTING = False
    ENV = 'development'

    SECRET_KEY = '\x14M\xf8B H\xe0g\x99/d\x7f\x84\xafI'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'mariia.utkinaa@gmail.com'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    MAIL_PASSWORD = 'ghuglsomjgettpnl'
    SALT = 'some salt'


class ProductionConfig(Config):
    ENV = 'production'
    SECRET_KEY = '\xa4\x00\xb1\xe3\xeb\x82\xdeI\xdb\x075\x11\xe0\x9a\xc3\xce_i\x18y\xb9\xd8\xa5\xfeIh|\x18w\xfa\x86'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
