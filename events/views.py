from django.shortcuts import render
from django.http import JsonResponse,Http404
from .models import event,workshop
from django.conf import settings
from urllib.parse import urljoin
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
DEPTS = [
    'CSE',
    'MCA',
    'ECE',
    'EEE',
    'MECH',
    'CIVIL',
    'ARCH',
    'GENERAL',
    'TH',
    'BTC',
]
@csrf_exempt
def eventList(req):
    dept = req.GET.get('dept',"")
    if(dept.upper() not in DEPTS):
        raise Http404()
    query = processImage(list(event.objects.filter(dept__iexact=dept).values(
        'name',
        'description',
        'reglink',
        'prize',
        'fees',
        'contacts',
        'image',
        'rules',
        'date',
        'time',
        'online'
        )))
    head = [{'name': x['name'],'image': x['image']} for x in query]
    return JsonResponse({'head':head,'body':query},safe=False)

@csrf_exempt
def workshopList(req):
    dept = req.GET.get('dept',"")
    if(dept.upper() not in DEPTS):
        raise Http404()
    query = processImage(list(workshop.objects.filter(dept__iexact=dept).values(
        'name',
        'description',
        'reglink',
        'fees',
        'contacts',
        'image',
        'date',
        'time'
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