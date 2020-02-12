from django.urls import path,include
from django.http import HttpResponse
urlpatterns = [
    path('',lambda x:HttpResponse('hello world')),
]
