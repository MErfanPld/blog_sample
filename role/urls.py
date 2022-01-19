from django.urls import path, include

urlpatterns = [
    path('api/', include('role.api.urls')),
]
