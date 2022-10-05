from msilib import init_database
from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    mobile_number = models.IntegerField()
    def __str__(self):
        return self.name

class Personn(models.Model):
    id = models.AutoField(primary_key=True),
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name_manu = models.CharField(max_length=255,default='SOMESTRING')
    def __str__(self):
        return self.name_manu

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    name_car = models.CharField(max_length=255,default=None)
    def __str__(self):
        return self.name_car