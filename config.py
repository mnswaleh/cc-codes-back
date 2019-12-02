"""Configure application"""
import os


class Config:
    """Default application configuration"""
    DEBUG = True  # Turns on debugging features in Flask
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Production application configuration"""
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """Development application configuration"""
    DEBUG = True


class TestingConfig(Config):
    """Testing application configuration"""
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
