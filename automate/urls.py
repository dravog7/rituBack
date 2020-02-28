from django.urls import path,include
from .views import addImage,testImage
urlpatterns = [
    path('addImage',addImage),
    path('',testImage),
]