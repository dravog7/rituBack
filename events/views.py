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
    'B.ARCH',
    'GENERAL',
    'TH',
    'BTC',
]
@csrf_exempt
def eventList(req):
    dept = req.GET.get('dept',"")
    if(dept.upper() not in DEPTS):
        raise Http404()
    query = processImage(list(event.objects.filter(dept__iexact=dept).order_by('id').values(
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
        'online',
        'preevent',
        'seats',
        'available',
        'category',
        )))
    category = list(set([x['category'] for x in query]))
    head = [{'name': x['name'],'image': x['image'],'category':x['category']} for x in query]
    return JsonResponse({'head':head,'category':category,'body':query},safe=False)

@csrf_exempt
def workshopList(req):
    dept = req.GET.get('dept',"")
    if(dept.upper() not in DEPTS):
        raise Http404()
    query = processImage(list(workshop.objects.filter(dept__iexact=dept).order_by('id').values(
        'name',
        'description',
        'reglink',
        'fees',
        'contacts',
        'image',
        'date',
        'time',
        'seats',
        'available'
        )))
    head = [{'name': x['name'],'image': x['image']} for x in query]
    return JsonResponse({'head':head,'body':query},safe=False)

def processImage(listi):
    for i in listi:
        i['image'] = urljoin(settings.MEDIA_URL,i['image'])

        i['contacts'] = json.loads(i['contacts'])

        if(i.get('rules',False)):
            i['rules'] = json.loads(i['rules'])

        if(i.get('prize',False)):
            i['prize'] = formatNumber(i['prize'])

    return listi

def formatNumber(num):
    if(num>=1000):
        if(num%1000==0):
            return f"{num//1000}K"
        else:
            return f"{num/1000}K"
    else:
        return f"{num}"