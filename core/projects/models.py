import os
from django.db import models
from django.db.models import Max
from django.db.models.signals import post_delete
from django.dispatch import receiver


def upload_to(instance, filename):
	# Get the current maximum number of images already uploaded
	max_id = Projects.objects.aggregate(Max('id'))['id__max'] or 0
	next_number = max_id + 1
	created_at = instance.created_at
	print(next_number, type(next_number))
	file_extension = filename.split('.')[-1]
	new_filename = f"{str(next_number)+'-prj'+str(created_at)}.{file_extension}"

	return os.path.join('media/projects_images', new_filename)


# Create your models here.
class Projects(models.Model):
	title = models.CharField(max_length = 250, verbose_name = 'Заголовок')
	summary = models.TextField(blank=True, verbose_name = 'Вкратце')
	content = models.TextField(blank=True, verbose_name = 'Контент')
	image = models.ImageField(upload_to=upload_to, blank=True, verbose_name = 'Обложка')
	period = models.CharField(max_length = 150, blank=True, verbose_name = 'Период')
	created_at = models.DateField(blank=True, verbose_name = 'Дата публикации')
	uploaded_at= models.DateTimeField(auto_now_add=True, blank=True)
	choosen = models.BooleanField(default=False, blank=True, verbose_name='Избранный')
	latitude = models.FloatField(default=0.0 ,blank=True, verbose_name='Широта(x)')
	longitude = models.FloatField(default=0.0, blank=True, verbose_name='Долгота(y)')
	

	class Meta:
		verbose_name = 'Проект'
		verbose_name_plural = 'Проекты'
	
	def __str__(self):
		return self.title


@receiver(post_delete, sender=Projects)
def delete_image_file(sender, instance, **kwargs):
	if instance.image:
		if os.path.isfile(instance.image.path):
			os.remove(instance.image.path)