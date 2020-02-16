from django.shortcuts import render
from django.http import JsonResponse
from .models import event
# Create your views here.

def listing(req):
    dept = req.GET.get('dept','')
    objs = event.objects.filter(dept=dept)
    return JsonResponse(list(objs.values('name','image')),safe=False)

def details(req):
    name = req.GET.get('name','')
    objs = event.objects.filter(name=name)
    return JsonResponse(list(objs.values('name','image','description','contacts','reglink','prize','dept')),safe=False)