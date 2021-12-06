from django.contrib.auth import views
from django.urls import path, include, re_path

from .views import (ArticleList,
                    ArticleCreate,
                    ArticleUpdate,
                    ArticleDelete,
                    Profile,
                    Login,
                    Register,
                    activate,
                    PasswordChangeView)

app_name = 'account'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    # re_path(
        # r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate, name='activate'),
    # re_path(r'^ratings/', include('star_ratings.urls', namespace='ratings')),

    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
]

urlpatterns += [
    path('', ArticleList.as_view(), name="home"),
    path('article/create', ArticleCreate.as_view(), name="create"),
    path('article/update/<int:pk>', ArticleUpdate.as_view(), name="update"),
    path('article/delete/<int:pk>', ArticleDelete.as_view(), name="delete"),
    path('profile/', Profile.as_view(), name="profile"),
]
