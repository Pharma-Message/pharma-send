from django.urls import path, include
from chat.views import chatpage
from django.contrib.auth.views import LoginView, LogoutView
 
 
urlpatterns = [
    path("", chatpage, name="chatpage"),
]