from decouple import config

class Config:
<<<<<<< HEAD
<<<<<<< HEAD
    SERVER_KEY = 'project'
    SERVER_NAME = 'local.host:80'
    
=======
    #Utilizar llave diference y alphanumeric
<<<<<<< HEAD
    SECRET_KEY = 'project'
<<<<<<< HEAD
<<<<<<< HEAD
    SERVER_NAME = 'local.docker:8000'
=======
    SECRET_KEY = 'codigofacilito' 
>>>>>>> parent of 4520eb3 (Update config.py)
=======
    SERVER_NAME = 'local.host'
>>>>>>> parent of 184f21c (Update config.py)
=======
    SERVER_NAME = 'local.docker:8000'
>>>>>>> parent of bcb5f94 (Update config.py)
=======
    #Utilizar llave diference y alphanumeric
    SECRET_KEY = 'project'
    SERVER_NAME = 'local.host:80'
>>>>>>> parent of 4d38943 (Update config.py)

>>>>>>> parent of bcb5f94 (Update config.py)
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://mildred:@localhost/project'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config('MAIL_USERNAME', default='test.mbrito@gmail.com')
    MAIL_PASSWORD = config('MAIL_USERNAME', default='TestMildredBrito123') #ALWAYS safer to create an environment variable

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://mildred:@localhost/project_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEST = True

class ProductionConfig(DevelopmentConfig):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'test': TestConfig,
    'production': ProductionConfig
}
