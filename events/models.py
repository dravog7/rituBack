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
filedefault=''
descdefault=''
namedefault=''

class event(models.Model):

    name = models.CharField(max_length=300,default=namedefault)
    description = models.TextField(default=descdefault)
    reglink = models.CharField(max_length=200,default='http://www.google.co.in')
    prize = models.IntegerField(default=0)
    fees = models.IntegerField(default=0)
    contacts = models.TextField(default="{}") #to easily add text. its JSON
    image = models.FileField(default=filedefault)
    dept = models.CharField(choices=DEPTS,max_length=10,default='CSE')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rules = models.TextField(default="{}")
    date = models.CharField(max_length=300,default="")
    time = models.CharField(max_length=300,default="")
    online = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class workshop(models.Model):
    name = models.CharField(max_length=300,default=namedefault)
    description = models.TextField(default=descdefault)
    reglink = models.CharField(max_length=200,default='http://www.google.co.in')
    fees = models.IntegerField(default=0)
    contacts = models.TextField(default="{}")
    image = models.FileField(default=filedefault)
    dept = models.CharField(choices=DEPTS,max_length=10)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.CharField(max_length=300,default="")
    time = models.CharField(max_length=300,default="")
    def __str__(self):
        return self.name