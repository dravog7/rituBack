from django.shortcuts import render
from django.http import JsonResponse
from .models import event
from django.conf import settings
from urllib.parse import urljoin
# Create your views here.

def listing(req):
    dept = req.GET.get('dept','')
    objs = event.objects.filter(dept=dept).values('name','image')
    return JsonResponse(processImage(list(objs)),safe=False)

def details(req):
    name = req.GET.get('name','')
    objs = event.objects.filter(name=name).values('name','image','description','contacts','reglink','prize','dept')
    return JsonResponse(processImage(list(objs)),safe=False)

def processImage(listi):
    for i in listi:
        i['image']=urljoin(settings.MEDIA_URL,i['image'])
    return listi