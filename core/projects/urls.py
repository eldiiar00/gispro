from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'projects'
urlpatterns = [
    path('', projects, name='projects'),
    path('project-<int:pk>', project, name='project'),
    # path('map-projects/', map_projects, name='map-projects'),

    path('api/projects', ProjectsAPIView.as_view(), name = 'api_projects'),
    path('api/project-<int:pk>', ProjectAPIView.as_view(), name='api_project'),
]