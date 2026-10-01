from . common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-%qb(qkb%2&$@14092t7oc@zsy^w&z0l&l%cmqf1f_k3^&^w0b7"

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-development-only-key')

# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "storefront3",
        "HOST": os.environ.get("DATABASE_HOST", "localhost"),
        "USER": os.environ.get("DATABASE_USER", "postgres"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD", "root"),
        "PORT": os.environ.get("DATABASE_PORT", "5432")
    }
}

ALLOWED_HOSTS = ['*']

CELERY_BROKER_URL = 'redis://redis:6379/1'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "TIMEOUT":10 * 60,  # 10 minutes
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

MAILERS = {
    "default": {
        "OPTIONS": {
            "host": "smtp4dev",
            "port": 25,
            "username": "",
            "password": "",
            "default_from_email": "from@milestone63.com",
        }
    }
}