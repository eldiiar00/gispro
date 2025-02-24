from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('', main, name='main'),
    
    path('api/main/', MainAPIView.as_view(), name='main_api'),
]