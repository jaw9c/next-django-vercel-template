from .base import *
import os
import dj_database_url

DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')
POSTGRES_URL= os.environ.get('POSTGRES_URL')

if POSTGRES_URL:
    DATABASES = {
        'default': dj_database_url.config(
            conn_max_age=600,
            conn_health_checks=True,
        ),
    }