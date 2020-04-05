from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from Lab5.views import log_in

urlpatterns = [
    path('', log_in),
    path('Lab5/', include('Lab5.urls')),
    path('admin/', admin.site.urls),
    path(r'session_security/', include('session_security.urls')),
]
