from django.conf.urls import include
from django.urls import path , include

urlpatterns = [
    #path('main/', views.circular3191 , name = 'circular3191'),
    path('api/',include('breeding_management.api.urls')),

]   # names should be string