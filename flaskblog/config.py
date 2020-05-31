import os


class Config:
    SECRET_KEY = "f16ba5e96df5fbbfad2a79c958d09526" #import secrets, secrets.token_hex(16) to get a random secret key via python
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")
