import os

from config.settings.base import *

DEBUG = True if os.environ.get("DEBUG", "True") == "True" else False
