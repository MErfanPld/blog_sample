from django.conf.urls import include
from django.urls import path, include

urlpatterns = [

    path('api/', include('finance.api.urls')),

]
# names should be string
