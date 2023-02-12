"""pharmasend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from accountforms.views import send_order_view, doctor_create, pharmacist_create, login_view, logout_view, acc_create, account_view, register_view
import pharmasend.settings

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'), 
    path('admin/', admin.site.urls),
    #path('accounts/', include('django.contrib.auth.urls')), 
    path('registration/', register_view, name='registration'),
    path('order/send', send_order_view, name="send_order"),
    path('accounts/login', login_view, name="login"),
    path('accounts/logout', logout_view, name="logout"),
    path('registration/account', acc_create, name='acc_registration'),
    path('registration/doctor', doctor_create, name='doctor_registration'),
    path('registration/pharmacist', pharmacist_create, name='pharmacist_registration'),
    path('registration/hospital', doctor_create, name='hospital_registration'),
    path('registration/account_view', account_view, name='acc_view'),
    path('chat/', include('chat.urls'))
    #path('registration/', TemplateView.as_view(template_name='registration.html'), name='registration')

]
