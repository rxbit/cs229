"""
WSGI config for cs229 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
import sys
import os
if not os.path.dirname(__file__) in sys.path[:1]:
    sys.path.insert(0, os.path.dirname(__file__))
# sys.path.append(os.path.abspath(os.path.dirname(__file__)))
# sys.path.append('/home/long/www')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cs229.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
