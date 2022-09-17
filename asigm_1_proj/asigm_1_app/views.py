import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.template import loader

def index(request):
    person_list = Person.objects.all()
    template = loader.get_template('index.html')
    context = {
        'person_list':person_list,
    }
    return HttpResponse(template.render(context,request))

def detail(request,id):
    template = loader.get_template('detail.html')
    person = Person.objects.get(id=id)
    context = {
        'person':person,
    }
    return HttpResponse(template.render(context,request))
