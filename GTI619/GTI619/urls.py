
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


urlpatterns = [
    # path('', include('frontend.urls')),
    path('Lab5/', include('Lab5.urls')),
    path('admin/', admin.site.urls),
]
