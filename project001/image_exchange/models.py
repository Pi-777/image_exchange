from django.db import models

# Create your models here.


class Picture(models.Model):
    name = models.CharField(max_length=2000)
    image_path = models.ImageField(upload_to='photos', default='user1.jpg')
    tag = models.CharField(max_length=2000, null=True)
