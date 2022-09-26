import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.template import loader
from .forms import RegisterForm
from django.contrib.auth.models import User

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

def register(request):
    if request.method == 'POST':
        response = HttpResponse()

        new_user = User(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
        new_user.save()

        response.write("<h1>Thanks for RES</h1></br>")
        response.write("Your username:" + request.POST['username'] + "</br>")
        response.write("Your email:" + request.POST['email'] + "</br>")
        return response

    registerForm = RegisterForm()
    return render(request,'register.html',{'form':registerForm})
