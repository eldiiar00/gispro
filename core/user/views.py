from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.shortcuts import render


from .models import *
from .serializers import UserLocationSerializer

def all_users(request):
	return render(request, 'user/all_users.html')

class UserLocationList(generics.ListAPIView):
	queryset = UserLocation.objects.all()
	serializer_class = UserLocationSerializer


class UserLocationCreate(APIView):
	def post(self, request):
		serializer = UserLocationSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
