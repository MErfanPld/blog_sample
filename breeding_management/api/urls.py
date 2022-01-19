from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [

     # ? ======================== delete ========================
     path('delete/daily-information/<int:pk>/', views.Daily_information_APIView_Delete.as_view(),
         name='delete daily information model'),
     path('delete/weightlifting/<int:pk>/', views.Weightlifting_APIVeiw_Delete.as_view(),
         name='delete weightlifting information model'),    
     path('delete/experiment-registration/<int:pk>/', views.ExperimentRegistration_APIVeiw_Delete.as_view(),
         name='delete blackoutprogramm model'),    
     path('delete/vaccin-registration/<int:pk>/', views.VaccineRegistration_APIVeiw_Delete.as_view(),
         name='delete vaccin registration information model'),    
     path('delete/drug-registration/<int:pk>/', views.DrugRegistration_APIVeiw_Delete.as_view(),
         name='delete drug registration information model'),    
     
     # ? ======================== update ========================
     path('update/daily-information/<int:pk>/', views.Daily_information_APIView_Update.as_view(),
         name='update daily information model'),
     path('update/weightlifting/<int:pk>/', views.Weightlifting_APIVeiw_Update.as_view(),
         name='update weightlifting information model'),    
     path('update/experiment-registration/<int:pk>/', views.ExperimentRegistration_APIVeiw_Update.as_view(),
         name='update blackoutprogramm model'),    
     path('update/vaccin-registration/<int:pk>/', views.VaccineRegistration_APIVeiw_Update.as_view(),
         name='update vaccin registration information model'),    
     path('update/drug-registration/<int:pk>/', views.DrugRegistration_APIVeiw_Update.as_view(),
         name='update drug registration information model'),    
     
    # ? ======================== list ========================
    path('list/daily-information/', views.Daily_information_APIView_List.as_view(),
         name='list daily information model'),
    path('list/weightlifting/', views.Weightlifting_APIVeiw_List.as_view(),
         name='list Weightlifting information model'),
    path('list/experimentregistration/', views.ExperimentRegistration_APIVeiw_List.as_view(),
         name='list experiment information model'),
    path('list/vaccinregistration/', views.VaccineRegistration_APIVeiw_List.as_view(),
         name='list vaccine information model'),
    path('list/drugregistration/', views.DrugRegistration_APIVeiw_List.as_view(),
         name='list drog information model'),

    # ? ======================== create ========================
    path('create/daily-information/', views.Daily_information_APIView.as_view(),
         name='create daily information model'),
    path('create/weightlifting/', views.Weightlifting_APIVeiw.as_view(),
         name='create Weightlifting information model'),
    path('create/experimentregistration/', views.ExperimentRegistration_APIVeiw.as_view(),
         name='create experiment information model'),
    path('create/vaccinregistration/', views.VaccineRegistration_APIVeiw.as_view(),
         name='create vaccine information model'),
    path('create/drugregistration/', views.DrugRegistration_APIVeiw.as_view(),
         name='create drog information model'),

]
