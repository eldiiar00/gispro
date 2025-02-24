import os
from django.db import models
from django.db.models import Max
from django.db.models.signals import post_delete
from django.dispatch import receiver


def upload_to(instance, filename):
	# Get the current maximum number of images already uploaded
	max_id = Partners.objects.aggregate(Max('id'))['id__max'] or 0
	next_number = max_id + 1
	print(next_number, type(next_number))
	file_extension = filename.split('.')[-1]
	new_filename = f"{str(next_number)+'-logo'}.{file_extension}"

	return os.path.join('media/partners', new_filename)


class Services(models.Model):
	title = models.CharField(max_length = 250, verbose_name = 'Наименование')
	summary = models.TextField(blank=True, verbose_name = 'Вкратце')
	description = models.TextField(blank=True, verbose_name = 'Описание')

	class Meta:
		verbose_name = 'Услуга'
		verbose_name_plural = 'Услуги'
	
	def __str__(self):
		return self.title


class Partners(models.Model):
	title = models.CharField(max_length = 250, verbose_name = 'Название')
	image = models.ImageField(upload_to=upload_to, blank=True, verbose_name = 'Логотип')
	description = models.TextField(blank=True, verbose_name = 'Описание')
	choosen = models.BooleanField(blank=True, default=False)

	class Meta:
		verbose_name = 'Партнер'
		verbose_name_plural = 'Партнеры'
	
	def __str__(self):
		return self.title


@receiver(post_delete, sender=Partners)
def delete_image_file(sender, instance, **kwargs):
	if instance.image:	
		if os.path.isfile(instance.image.path):
			os.remove(instance.image.path)