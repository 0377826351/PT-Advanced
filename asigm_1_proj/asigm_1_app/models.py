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