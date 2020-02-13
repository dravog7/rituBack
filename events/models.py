from django.db import models

# Create your models here.
class event(models.Model):
    name = models.CharField()
    description = models.TextField()
    reglink = models.URLField()
    prize = models.IntegerField()
    contacts = models.TextField() #to easily add text. its JSON
    image = models.ImageField()