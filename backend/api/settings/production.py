from .base import *
import os
import dj_database_url

DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASE_URL= os.environ.get('DATABASE_URL')

if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(
            conn_max_age=600,
            conn_health_checks=True,
        ),
    }