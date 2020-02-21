from django.db import models
from django.contrib.auth.models import User
# Create your models here.
DEPTS = [
    ('CSE','CSE'),
    ('MCA','MCA'),
    ('ECE','ECE'),
    ('EEE','EEE'),
    ('Mech','Mech'),
    ('Civil','Civil'),
    ('Arch','Arch'),
    ('General','General'),
]
class event(models.Model):

    name = models.CharField(max_length=300)
    description = models.TextField()
    reglink = models.URLField(default='http://www.google.co.in')
    prize = models.IntegerField()
    contacts = models.TextField(default="{}") #to easily add text. its JSON
    image = models.FileField()
    dept = models.CharField(choices=DEPTS,max_length=10)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rules = models.TextField(default="{}")
    def __str__(self):
        return self.name

class workshop(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    reglink = models.URLField(default='http://www.google.co.in')
    fees = models.IntegerField()
    contacts = models.TextField(default="{}")
    image = models.FileField()
    dept = models.CharField(choices=DEPTS,max_length=10)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name