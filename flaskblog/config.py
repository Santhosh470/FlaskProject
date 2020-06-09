import os

class Config:
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT =  587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL")
    MAIL_PASSWORD = os.environ.get("PASSWORD")
    #MAIL_SUPPRESS_SEND = False
    #MAIL_DEBUG = True
    MAIL_DEFAULT_SENDER = 'noreply@blog.com'
    SECRET_KEY = 'c782a0280cb2ba42f041536f07a002a8'
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"

