"""
URL configuration for pj_tracoll project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# URL matching from PROJECT LEVEL TO APPLICATION LEVEL
from django.urls import include
urlpatterns += [path('app_tracoll/', include('app_tracoll.urls')),]

# URL MAPPING USED TO redirect to app_tracoll when receive empty URL
from django.views.generic import RedirectView
urlpatterns += [ path('', RedirectView.as_view(url='app_tracoll/')),]

# Redirect to home URL after login
LOGIN_REDIRECT_URL = '/'

# Redirect Django-generated emails to console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# adds 8 urls automatically generated by Django to handle login / logout, etc
urlpatterns += [ path('accounts/', include('django.contrib.auth.urls')), ]

