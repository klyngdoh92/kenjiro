from config.settings.base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "db_name",
        "USER": "user",
        "PASSWORD": "pwd",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
