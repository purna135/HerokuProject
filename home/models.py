from django.db import models

# Create your models here.
class Images(models.Model):
    photo = models.ImageField(upload_to='images')
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)