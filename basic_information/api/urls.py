from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [


     # ? ======================== delete ========================
     path('delete/vaccin/<int:pk>/', views.Vaccin_APIView_Delete.as_view(),
         name='delete vaccin model'),
     path('delete/owner-information/<int:pk>/', views.OwnerInformation_APIView_Delete.as_view(),
         name='delete owner information model'),    
     path('delete/blackout-programm/<int:pk>/', views.BlackoutProgram_APIView_Delete.as_view(),
         name='delete blackoutprogramm model'),    
     path('delete/chicken-information/<int:pk>/', views.ChickenInformation_APIView_Delete.as_view(),
         name='delete chicken information model'),    
     path('delete/farm-information/<int:pk>/', views.FarmInformation_APIView_Delete.as_view(),
         name='delete farm information model'),    
     path('delete/standard-information/<int:pk>/', views.StandardInformation_APIView_Delete.as_view(),
         name='delete standard infotmaion model'),    
     path('delete/vaccin-programm-informaion/<int:pk>/', views.VaccineProgramInformation_APIView_Delete.as_view(),
         name='delete vaccin model'),    
     path('delete/duration-information/<int:pk>/', views.DurationInformation_APIView_Delete.as_view(),
         name='delete duration model'),    
     path('delete/hall-information/<int:pk>/', views.HallInformation_APIView_Delete.as_view(),
         name='delete hall information model'),    
     path('delete/dietplan/<int:pk>/', views.DietPlan_APIView_Delete.as_view(),
         name='delete dietplan model'),    
     path('delete/storeroom/<int:pk>/', views.StoreRoom_APIView_Delete.as_view(),
         name='delete storeroom model'),    




     # ? ======================== update ========================
     path('update/vaccin/<int:pk>/', views.Vaccin_APIView_Update.as_view(),
         name='update vaccin model'),
     path('update/owner-information/<int:pk>/', views.OwnerInformation_APIView_Update.as_view(),
         name='update owner information model'),    
     path('update/blackout-programm/<int:pk>/', views.BlackoutProgram_APIView_Update.as_view(),
         name='update blackoutprogramm model'),    
     path('update/chicken-information/<int:pk>/', views.ChickenInformation_APIView_Update.as_view(),
         name='update chicken information model'),    
     path('update/farm-information/<int:pk>/', views.FarmInformation_APIView_Update.as_view(),
         name='update farm information model'),    
     path('update/standard-information/<int:pk>/', views.StandardInformation_APIView_Update.as_view(),
         name='update standard infotmaion model'),    
     path('update/vaccin-programm-informaion/<int:pk>/', views.VaccineProgramInformation_APIView_Update.as_view(),
         name='update vaccin model'),    
     path('update/duration-information/<int:pk>/', views.DurationInformation_APIView_Update.as_view(),
         name='update duration model'),    
     path('update/hall-information/<int:pk>/', views.HallInformation_APIView_Update.as_view(),
         name='update hall information model'),    
     path('update/dietplan/<int:pk>/', views.DietPlan_APIView_Update.as_view(),
         name='update dietplan model'),    
     path('update/storeroom/<int:pk>/', views.StoreRoom_APIView_Update.as_view(),
         name='update storeroom model'),    


    # ? ======================== list ========================
    path('list/owner-information/', views.OwnerInformation_APIView_List.as_view(),
         name='list owner information model'),
    path('list/blackout-programm/', views.BlackoutProgram_APIView_List.as_view(),
         name='list blackout model'),
    path('list/chicken-information/', views.ChickenInformation_APIView_List.as_view(),
         name='list chicken information model'),
    path('list/farm-information/', views.FarmInformation_APIView_List.as_view(),
         name='list farm information model'),
    path('list/standard-information/', views.StandardInformation_APIView_List.as_view(),
         name='list standard information model'),
    path('list/vaccin-program-information/', views.VaccineProgramInformation_APIView_List.as_view(),
         name='list vaccin information model'),
    path('list/duration-information/', views.DurationInformation_APIView_List.as_view(),
         name='list duration information model'),
    path('list/hall-information/', views.HallInformation_APIView_List.as_view(),
         name='list hall information model'),
    path('list/dietplan/', views.DietPlan_APIView_List.as_view(),
         name='list diet information model'),
    path('list/storeroom/', views.StoreRoom_APIView_List.as_view(),
         name='list store room model '),
    path('list/vaccin/', views.Vaccin_APIView_List.as_view(),
         name='list vaccin model '),

    # ? ======================== create ========================
    path('create/owner-information/', views.OwnerInformation_APIView.as_view(),
         name='create owner information model'),
    path('create/blackout-programm/', views.BlackoutProgram_APIView.as_view(),
         name='create blackout model'),
    path('create/chicken-information/', views.ChickenInformation_APIView.as_view(),
         name='create chicken information model'),
    path('create/farm-information/', views.FarmInformation_APIView.as_view(),
         name='create farm information model'),
    path('create/standard-information/', views.StandardInformation_APIView.as_view(),
         name='create standard information model'),
    path('create/vaccin-program-information/', views.VaccineProgramInformation_APIView.as_view(),
         name='create vaccin information model'),
    path('create/duration-information/', views.DurationInformation_APIView.as_view(),
         name='create duration information model'),
    path('create/hall-information/', views.HallInformation_APIView.as_view(),
         name='create hall information model'),
    path('create/dietplan/', views.DietPlan_APIView.as_view(),
         name='create diet information model'),
    path('create/storeroom/', views.StoreRoom_APIView.as_view(),
         name='create store room model '),
    path('create/vaccin/', views.Vaccin_APIView.as_view(),
          name='create vaccin table to store name and type of them')
]
