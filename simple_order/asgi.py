"""
ASGI config for simple_order project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from configurations.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_order.settings')
os.environ.setdefault("DJANGO_CONFIGURATION", "Production")

application = get_asgi_application()
