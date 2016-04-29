"""
Django settings for glue project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG', False)

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'glue_auth',
    'rest_framework',
    'price_monitor',
    'price_monitor.product_advertising_api',
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'glue.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'glue.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': '5432',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/srv/static/'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(filename)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, '..', 'logs', 'error.log'),
            'formatter': 'verbose',
        },
        'price_monitor': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, '..', 'logs', 'price_monitor.log'),
            'formatter': 'verbose',
        },
        'price_monitor.product_advertising_api': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, '..', 'logs', 'price_monitor.product_advertising_api.log'),
            'formatter': 'verbose',
        },
        'price_monitor.tasks': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, '..', 'logs', 'price_monitor.tasks.log'),
            'formatter': 'verbose',
        },
        'price_monitor.utils': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, '..', 'logs', 'price_monitor.utils.log'),
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file_error', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'price_monitor': {
            'handlers': ['price_monitor'],
            'level': 'INFO',
            'propagate': True,
        },
        'price_monitor.product_advertising_api': {
            'handlers': ['price_monitor.product_advertising_api'],
            'level': 'INFO',
            'propagate': True,
        },
        'price_monitor.tasks': {
            'handlers': ['price_monitor.tasks'],
            'level': 'INFO',
            'propagate': True,
        },
        'price_monitor.utils': {
            'handlers': ['price_monitor.utils'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# caching
# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.RedisCache',
#         'LOCATION': 'redis',
#         'OPTIONS': {
#             'DB': 0,
#             'PARSER_CLASS': 'redis.connection.HiredisParser',
#             'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
#             'CONNECTION_POOL_CLASS_KWARGS': {
#                 'max_connections': 50,
#                 'timeout': 20,
#             }
#         },
#     },
# }
# CACHE_MIDDLEWARE_KEY_PREFIX = 'pm_glue'

# glue login
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'

# E-Mail
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')  # smtp is the Django default
if EMAIL_BACKEND == 'django.core.mail.backends.smtp.EmailBackend':
    EMAIL_HOST = os.environ.get('EMAIL_HOST')
    EMAIL_PORT = os.environ.get('EMAIL_PORT')
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    EMAIL_USE_TSL = os.environ.get('EMAIL_USE_TSL', True)
elif EMAIL_BACKEND == 'django.core.mail.backends.filebased.EmailBackend':
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, '..', 'logs', 'emails.out')

# Celery
CELERY_ACCEPT_CONTENT = ['pickle', 'json']
BROKER_URL = os.environ.get('BROKER_URL')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', '')
CELERY_CHORD_PROPAGATES = True
# redis specific, see http://celery.readthedocs.io/en/latest/getting-started/brokers/redis.html#caveats
BROKER_TRANSPORT_OPTIONS = {
    'fanout_prefix': True,
    'fanout_patterns': True,
}

# price_monitor
PRICE_MONITOR_BASE_URL = os.environ.get('PRICE_MONITOR_BASE_URL', 'http://0.0.0.0:8000')
PRICE_MONITOR_AWS_ACCESS_KEY_ID = os.environ.get('PRICE_MONITOR_AWS_ACCESS_KEY_ID', '')
PRICE_MONITOR_AWS_SECRET_ACCESS_KEY = os.environ.get('PRICE_MONITOR_AWS_SECRET_ACCESS_KEY', '')
PRICE_MONITOR_AMAZON_PRODUCT_API_REGION = os.environ.get('PRICE_MONITOR_AMAZON_PRODUCT_API_REGION', 'DE')
PRICE_MONITOR_AMAZON_PRODUCT_API_ASSOC_TAG = os.environ.get('PRICE_MONITOR_AMAZON_PRODUCT_API_ASSOC_TAG', '')
PRICE_MONITOR_AMAZON_ASSOCIATE_NAME = 'John Doe'
PRICE_MONITOR_AMAZON_ASSOCIATE_SITE = 'Amazon.de'
PRICE_MONITOR_EMAIL_SENDER = 'Amazon Pricemonitor <pm@localhost>'
PRICE_MONITOR_SITENAME = 'Pricemonitor Site'
# refresh product after 1 hours
PRICE_MONITOR_AMAZON_PRODUCT_REFRESH_THRESHOLD_MINUTES = os.environ.get('PRICE_MONITOR_AMAZON_PRODUCT_REFRESH_THRESHOLD_MINUTES', 60)
# time after when to notify about a subscription again
PRICE_MONITOR_SUBSCRIPTION_RENOTIFICATION_MINUTES = os.environ.get('PRICE_MONITOR_SUBSCRIPTION_RENOTIFICATION_MINUTES', 24 * 3 * 60)

REST_FRAMEWORK = {
    'PAGINATE_BY': 50,
    'PAGINATE_BY_PARAM': 'page_size',  # Allow client to override, using `?page_size=xxx`.
    'MAX_PAGINATE_BY': 100  # Maximum limit allowed when using `?page_size=xxx`.
}
