from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *
from projects.models import Projects
from projects.serializers import ProjectsSerializer
from news.models import News
from news.serializers import NewsSerializer


def main(request):
	last_news = News.objects.all().order_by('-created_at')[:3]
	services = Services.objects.all()
	chosen_projects = Projects.objects.filter(choosen=True)
	partners = Partners.objects.all()
	context = {'last_news':last_news,'services':services,'chosen_projects': chosen_projects, 'partners':partners}
	print(last_news)
	return render(request, 'main/main.html',context)


class MainAPIView(APIView):
	def get(self, request):
		last_news = News.objects.all().order_by('-created_at')[:3]
		services = Services.objects.all()
		chosen_projects = Projects.objects.filter(choosen=True)
		partners = Partners.objects.all()

		# serializing
		news_serializer = NewsSerializer(last_news, many=True)
		services_serializer = ServicesSerializer(services, many=True)
		projects_serializer = ProjectsSerializer(chosen_projects, many=True)
		partners_serializer = PartnersSerializer(partners, many=True)

		# return data in JSON
		return Response({
			'last_news': news_serializer.data,
			'services': services_serializer.data,
			'chosen_projects': projects_serializer.data,
			'partners': partners_serializer.data
		})