"""
WSGI config for actividades_project project.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'actividades_project.settings')

application = get_wsgi_application()
