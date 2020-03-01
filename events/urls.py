from django.urls import path,include
from django.http import HttpResponse
from .views import eventList,workshopList
urlpatterns = [
    path('',lambda x:HttpResponse('hello world')),
    path('events',eventList),
    path('workshops',workshopList),
]
