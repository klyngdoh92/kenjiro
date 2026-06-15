import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from config.settings.base import *

DEBUG = False


SENTRY_DSN = os.getenv("SENTRY_DSN")
if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[
            DjangoIntegration(),
        ],
        # Add data like request headers and IP for users,
        # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
        traces_sample_rate=0.1,
        send_default_pii=True,
    )
