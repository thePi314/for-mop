"""
ASGI config for mop_test project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

django_rest_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mop_test.settings')

application = ProtocolTypeRouter({
    "http": django_rest_app
})
