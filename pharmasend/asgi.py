"""
ASGI config for pharmasend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pharmasend.settings')

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing
from django.urls import path, include
import os
import django

django.setup()

application = get_asgi_application()
#application = ProtocolTypeRouter(
#    {
#        "http" : get_asgi_application(),
#        "https" : get_asgi_application(),
#        "websocket" : AuthMiddlewareStack(
#            URLRouter(
#                chat.routing.websocket_urlpatterns
#            )
#        )
#    }
#)

