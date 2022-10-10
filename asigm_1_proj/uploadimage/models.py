from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title

class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    color = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name