from .base import *

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'botparty', 
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}
