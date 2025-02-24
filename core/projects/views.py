from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
import json

from .models import *
from .serializers import *


def projects(request):
	projects = Projects.objects.all()
	projects_json = json.dumps([
        {'title': project.title, 'x': project.latitude, 'y': project.longitude, 
    	'id':project.id , 'img': project.image.url}
        for project in projects
    ])
	return render(request, 'projects/projects.html', 
		{'projects': projects, 'projects_json': projects_json})

def project(request, pk):
	project = Projects.objects.get(id=pk)
	return render(request, 'projects/project.html', {'project': project})

# def map_projects(request, pk):
# 	projects = Projects.objects.all()
# 	return render(request, 'projects/map_projects.html', {'projects': projects})


class ProjectsAPIView(APIView):
	def get(self, request):
		projects = Projects.objects.all()
		
		projects_serializer = ProjectsSerializer(projects, many=True)

		# return data in JSON
		return Response({
			'projects': projects_serializer.data,
		})


class ProjectAPIView(RetrieveAPIView):
	queryset = Projects.objects.all()
	serializer_class = ProjectsSerializer
	lookup_field = 'pk'