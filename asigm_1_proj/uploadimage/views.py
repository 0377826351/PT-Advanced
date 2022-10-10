import re
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Image,Animal
from .forms import AnimalForm

def index(request):
    template = loader.get_template('uploadimage.html')
    if request.method == 'POST':
        new_img = Image(title=request.POST['title'],image=request.FILES['img'])
        new_img.save()
    context = {
        'obj':'ga'
    }
    return HttpResponse(template.render(context,request))

def animal(request):
    template = loader.get_template('animal.html')
    if request.method == 'POST':
        new_animal = Animal(name=request.POST['name'],age=request.POST['age'],color=request.POST['color'])
        new_animal.save()
    context = {
        'form': AnimalForm()
    }
    return HttpResponse(template.render(context,request))
