from django.db import models

# Create your models here.

class airfield(models.model):
    airfield_name=models.charfield(max_length=150)
    airfield_cityname=models.charfield(max_length=250)


class fly(models.model):
    starting-city=models.charfield(max_length=200)
    starting-airfield=models.charfield(max_length=150)
    destination-city=models.charfield(max_length=200)
    destination-airfield=models.charfield(max_length=150)
    d-time=models.datetimefield()
    price=models.floatfield()
    transport=models.charfield(max_length=200)


class airplane(models.model):
    plane=models.charfield(max_length=100)
    volume=models.integerfield()

class transport(models.model):
    rank=models.integerfield()
    company=models.charfield(max_length=100)


