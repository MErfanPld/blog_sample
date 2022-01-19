from django.conf.urls import url
from django.urls import path , include
from . import views

urlpatterns = [
    
    path('register/owner/' , views.User_APIView.as_view() , name='register owner information model') ,
    path('api-auth/', include('rest_framework.urls')),   
]