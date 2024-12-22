from .base import *
import os
import dj_database_url

DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_DATABASE = os.environ.get('POSTGRES_DATABASE')

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": POSTGRES_DATABASE,
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWORD,
        "HOST": POSTGRES_HOST,
        "PORT": 5432,
    }
}