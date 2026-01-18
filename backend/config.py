import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key")

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-super-secret-key")

    SQLALCHEMY_DATABASE_URI = (
        "postgresql://ems_user:strongpassword@localhost:5432/ems_db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SENDER = "xelortop1@gmail.com"
    MAIL_PASSWORD = "eipv qafz rsyq ybnm"
