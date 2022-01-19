"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.authtoken.views import ObtainAuthToken  # note : delete get method


urlpatterns = [
    path('admin/', admin.site.urls),
    path('breeding/', include('breeding_management.urls')),
    path('basic-information/', include('basic_information.urls')),
    path('finance/', include('finance.urls')),
    path('role/', include('role.urls')),
    path('user/', include('usermanager.urls')),
    path('login/', ObtainAuthToken.as_view()),  # login
]
