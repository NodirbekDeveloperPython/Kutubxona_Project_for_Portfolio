from django.contrib import admin
from django.urls import path, include
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('asosiy.urls')),
]
