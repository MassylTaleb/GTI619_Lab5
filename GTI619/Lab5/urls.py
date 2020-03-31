from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views
from rest_framework import routers
from .api import *
router = routers.DefaultRouter()
router.register('api/params', ParamsViewSet, 'params')
router.register('api/profile', ProfileViewSet, 'profile')

urlpatterns = router.urls