"""
WSGI config for ambassador project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/

Use  ./manage.py collectstatic  to collect static files when running locally.  This is auto done when hosted in Heroku.
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ambassador.settings")

application = Cling(get_wsgi_application())
