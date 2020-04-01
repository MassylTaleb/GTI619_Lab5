from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views
from .views import ActivateAccount
from rest_framework import routers
from .api import *

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.log_in, name='login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('params/', views.params, name='params'),
    path('allCR/', views.getAllCR, name='allCR'),
    path('allCA/', views.getAllCA, name='allCA'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
]