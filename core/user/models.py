from django.db import models
from django.contrib.auth.models import AbstractUser


# class CustomUser(AbstractUser):
# 	pass

class UserLocation(models.Model):
	user_id = models.CharField(max_length=255, unique=True, verbose_name = 'ID (идентификатор)')
	user_nickname = models.CharField(max_length=255, verbose_name = 'Никнейм')
	latitude = models.FloatField(verbose_name='Широта(x)')
	longitude = models.FloatField(verbose_name='Долгота(y)')
	timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Временная метка')

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'
	
	def __str__(self):
		return self.user_nickname


# class UserTrakcer(AbstractUser):
# 	user_locations = models.ManyToManyField(UserLocation)