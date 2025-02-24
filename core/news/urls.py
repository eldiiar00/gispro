from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'news'
urlpatterns = [
    path('', all_news, name = 'all_news'),
    path('one_news-<int:pk>', one_news, name='one_news'),

    path('api/all_news', AllNewsAPIView.as_view(), name = 'api_all_news'),
    path('api/one_news-<int:pk>', OneNewsAPIView.as_view(), name='api_one_news'),
]