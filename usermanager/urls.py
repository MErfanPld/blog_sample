from django.conf.urls import include
from django.urls import path , include

urlpatterns = [
    path('api/',include('usermanager.api.urls')),

]   # names should be string