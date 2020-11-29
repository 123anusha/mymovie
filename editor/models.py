from django.db import models

# Create your models here.
class NewMovie(models.Model):
    image = models.ImageField(upload_to='movie/', null=True)
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=20)
    cast = models.CharField(max_length=100)
    movie_type = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    res_date = models.DateField(null=True)
    description = models.TextField()
