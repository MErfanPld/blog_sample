from django.conf.urls import include
from django.urls import path , include

urlpatterns = [
    path('api/',include('basic_information.api.urls')),

]   # names should be string