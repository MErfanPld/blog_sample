from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    # ? ======================== create ========================
    path('create/role/name/', views.CreateAPIView.as_view(),
         name='create_role_model'),
    path('create/role/', views.CreateRoleView.as_view(),
         name='create_role'),
]
