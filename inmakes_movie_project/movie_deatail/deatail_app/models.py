from django.db import models

# Create your models here.
class movies(models.Model):
    name=models.CharField(max_length=123)
    year=models.IntegerField()
    discription=models.TextField()
    movie_image=models.ImageField(upload_to='movie_images')