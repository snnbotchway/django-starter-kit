from .common import *

DEBUG = True

SECRET_KEY = "change_me"

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "devdb",
        "USER": "postgres",
        "PASSWORD": "change_me",
        "HOST": "db",
        "PORT": "5432",
    }
}
