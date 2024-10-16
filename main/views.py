from django.shortcuts import render
from .models import *

def HomePage(request):
    url=Video_save.objects.all()
    for i in url:
        url1=i.video_file.url
    return render(request, 'index.html', {"url":url1})

# Create your views here.
