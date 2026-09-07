import os
import dj_database_url
from . common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['milestone63-prod-72e404496595.herokuapp.com']

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL")
    )
}

REDIS_URL = os.environ['REDIS_URL']

CELERY_BROKER_URL = REDIS_URL

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "TIMEOUT":10 * 60,  # 10 minutes
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

MAILERS = {
    "default": {
        "OPTIONS": {
            "host": os.environ['MAILGUN_SMTP_SERVER'],
            "port": os.environ['MAILGUN_SMTP_PORT'],
            "username": os.environ['MAILGUN_SMTP_LOGIN'],
            "password": os.environ['MAILGUN_API_KEY'],
        }
    }
}