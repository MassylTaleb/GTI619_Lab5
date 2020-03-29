from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('params/', views.params, name='params'),

]