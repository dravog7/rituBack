from django.shortcuts import render
from django.http import JsonResponse,Http404
from .models import event,workshop
from django.conf import settings
from urllib.parse import urljoin
import json
# Create your views here.
DEPTS = [
    'CSE',
    'MCA',
    'ECE',
    'EEE',
    'Mech',
    'Civil',
    'Arch',
    'General'
]
def eventList(req):
    dept = req.GET.get('dept',False)
    if(dept not in DEPTS):
        raise Http404()
    query = processImage(list(event.objects.filter(dept=dept).values(
        'name',
        'description',
        'reglink',
        'prize',
        'contacts',
        'image',
        'rules'
        )))
    head = [{'name': x['name'],'image': x['image']} for x in query]
    return JsonResponse({'head':head,'body':query},safe=False)
    
def workshopList(req):
    dept = req.GET.get('dept',False)
    if(dept not in DEPTS):
        raise Http404()
    query = processImage(list(workshop.objects.filter(dept=dept).values(
        'name',
        'description',
        'reglink',
        'fees',
        'contacts',
        'image',
        )))
    head = [{'name': x['name'],'image': x['image']} for x in query]
    return JsonResponse({'head':head,'body':query},safe=False)

def processImage(listi):
    for i in listi:
        i['image']=urljoin(settings.MEDIA_URL,i['image'])
        i['contacts']=json.loads(i['contacts'])
        if(i.get('rules',False)):
            i['rules']=json.loads(i['rules'])
    return listi