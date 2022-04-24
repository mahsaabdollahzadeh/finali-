from django.db import models

# Create your models here.

class airfield(models.Model):
    airfield_name=models.CharField(max_length=150)
    airfield_cityname=models.CharField(max_length=250)


class fly(models.Model):
    city_start = models.CharField(max_length=200)
    airfield_start = models.CharField(max_length=150)
    destination_city = models.CharField(max_length=200)
    destination_airfield = models.CharField(max_length=150)
    d_time = models.DateTimeField()
    price = models.FloatField()
    transport = models.CharField(max_length=200)


class airplane(models.Model):
    plane=models.CharField(max_length=100)
    volume=models.IntegerField()

class transport(models.Model):
    rank=models.IntegerField()
    company=models.CharField(max_length=100)


