from django.urls import path
from .views import *

app_name = 'user'
urlpatterns = [
    path('', all_users, name='all_users'),
    path('api/user_locations/list/', UserLocationList.as_view(), name='user_locations'),
    path('api/user_locations/create/', UserLocationCreate.as_view(), name='user_location_create'),

]