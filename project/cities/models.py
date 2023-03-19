from django.db import models
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    content = models.TextField(verbose_name='Описание')
    img = models.ImageField(upload_to='uploads/', default=0, null=True, blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('cities:home')
# Create your models here.
