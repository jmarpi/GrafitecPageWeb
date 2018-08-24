from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    path('admin/', include(admin.site.urls) ),
    path(r'', include('clientPage.urls')),
]
