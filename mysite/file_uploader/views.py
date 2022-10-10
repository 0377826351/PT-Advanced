from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from .forms import UploadFileForm

def fileUploaderView(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            upload(request.FILES['file'])
            return HttpResponse("<h2> Success </h2>")
        else:
            return HttpResponse("<h2> False </h2>")

    form = UploadFileForm()
    context = {
        'form': form,
    }
    return render(request,'fileUploader.html',context)

def upload(f):
    file = open(f.name,'wb+')
    for chunk in f.chunks():
        file.write(chunk)
