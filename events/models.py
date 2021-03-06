from django.db import models
from django.contrib.auth.models import User
from automate.models import Image
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
filedefault='https://testhttp1234.blob.core.windows.net/media/about-ritu_ft9zmHG.jpg'
descdefault=""
namedefault=""
contactdefault='[{"name":"name","mob":0}]'
ruledefault="[]"
class event(models.Model):

    name = models.CharField(max_length=300,default=namedefault)
    description = models.TextField(default=descdefault)
    reglink = models.CharField(max_length=200,default='http://www.google.co.in')
    prize = models.IntegerField(default=0)
    fees = models.IntegerField(default=0)
    contacts = models.TextField(default=contactdefault) #to easily add text. its JSON
    image = models.FileField(blank=True,null=True)
    ImageFrom = models.ForeignKey(Image,blank=True,null=True,on_delete=models.CASCADE)
    dept = models.CharField(choices=DEPTS,max_length=10,default='General')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rules = models.TextField(default=ruledefault)
    date = models.CharField(max_length=300,default="")
    time = models.CharField(max_length=300,default="")
    online = models.BooleanField(default=False)
    preevent = models.BooleanField(default=False)
    seats = models.IntegerField(default=-1)
    available = models.IntegerField(default=-1)
    def __str__(self):
        return self.name

class workshop(models.Model):
    name = models.CharField(max_length=300,default=namedefault)
    description = models.TextField(default=descdefault)
    reglink = models.CharField(max_length=200,default='http://www.google.co.in')
    fees = models.IntegerField(default=0)
    contacts = models.TextField(default=contactdefault)
    image = models.FileField(blank=True,null=True)
    ImageFrom = models.ForeignKey(Image,blank=True,null=True,on_delete=models.CASCADE)
    dept = models.CharField(choices=DEPTS,max_length=10)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.CharField(max_length=300,default="")
    time = models.CharField(max_length=300,default="")
    seats = models.IntegerField(default=-1)
    available = models.IntegerField(default=-1)
    def __str__(self):
        return self.name
