from django.db import models

# Create your models here.

class musician(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=200)

class album(models.Model):
    artist =models.ForeignKey(musician,on_delete=models.CASCADE)
    name = models.CharField(max_length= 100)
    release_data = models.DateField()
    num_stars = models.IntegerField()

