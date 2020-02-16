from django.urls import path,include
from django.http import HttpResponse
from .views import listing,details
urlpatterns = [
    path('',lambda x:HttpResponse('hello world')),
    path('list',listing),
    path('details',details),
]
