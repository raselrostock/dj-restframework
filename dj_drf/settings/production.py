from .base import *

################################
##     BASE CONFIGURATION     ##
################################
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = bool(os.environ.get("DEBUG", False))
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']

################################
##    DATABASE CONFIGURATION  ##
################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

####################################
##  PASSWORD CONFIGURATION ##
####################################
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]