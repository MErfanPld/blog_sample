from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [

     # ? ======================== delete ========================
     path('delete/cost/<int:pk>/', views.Cost_APIView_Delete.as_view(),
         name='delete cost model'),
     path('delete/debtore/<int:pk>/', views.Debtor_APIVeiw_Delete.as_view(),
         name='delete debtore model'),    
     path('delete/income/<int:pk>/', views.Income_APIVeiw_Delete.as_view(),
         name='delete income model'),    
     path('delete/creditore/<int:pk>/', views.Creditor_APIVeiw_Delete.as_view(),
         name='delete creditore information model'),   
     

     # ? ======================== update ========================
     path('update/cost/<int:pk>/', views.Cost_APIView_Update.as_view(),
         name='update cost model'),
     path('update/debtore/<int:pk>/', views.Debtor_APIVeiw_Update.as_view(),
         name='update debtore model'),    
     path('update/income/<int:pk>/', views.Income_APIVeiw_Update.as_view(),
         name='update income model'),    
     path('update/creditore/<int:pk>/', views.Creditor_APIVeiw_Update.as_view(),
         name='update creditore information model'),   
     
    # ? ======================== list ========================
    path('list/cost/', views.Cost_APIView_List.as_view(),
         name='list cost information model'),
    path('list/debtor/', views.Debtor_APIVeiw_List.as_view(),
         name='list debtor information model'),
    path('list/income/', views.Income_APIVeiw_List.as_view(),
         name='list income information model'),
    path('list/creditor/', views.Creditor_APIVeiw_List.as_view(),
         name='list creditor information model'),

    # ? ======================== create ========================
    path('create/cost/', views.Cost_APIView.as_view(),
         name='create cost information model'),
    path('create/debtor/', views.Debtor_APIVeiw.as_view(),
         name='create debtor information model'),
    path('create/income/', views.Income_APIVeiw.as_view(),
         name='create income information model'),
    path('create/creditor/', views.Creditor_APIVeiw.as_view(),
         name='create creditor information model'),

]
