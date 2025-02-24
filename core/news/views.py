from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView

from .models import *
from .serializers import *

def all_news(request):
	all_news = News.objects.all().order_by('-created_at')
	return render(request, 'news/all_news.html', {'all_news': all_news})

def one_news(request, pk):
	one_news = News.objects.get(id=pk)
	return render(request, 'news/one_news.html', {'one_news': one_news})


class AllNewsAPIView(APIView):
	def get(self, request):
		all_news = News.objects.all()
		
		news_serializer = NewsSerializer(all_news, many=True)

		# return data in JSON
		return Response({
			'all_news': news_serializer.data,
		})


class OneNewsAPIView(RetrieveAPIView):
	queryset = News.objects.all()
	serializer_class = NewsSerializer
	lookup_field = 'pk'