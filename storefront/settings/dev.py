from . common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-%qb(qkb%2&$@14092t7oc@zsy^w&z0l&l%cmqf1f_k3^&^w0b7"

# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "storefront3",
        "HOST": "localhost",
        "USER": "postgres",
        "PASSWORD": "root",
        "PORT": "5432"
    }
}