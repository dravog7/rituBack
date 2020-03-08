from django.db import models
from django.contrib.auth.models import User
from automate.models import Image
from django.utils import timezone
# Create your models here.
DEPTS = [
    ('CSE','CSE'),
    ('MCA','MCA'),
    ('ECE','ECE'),
    ('EEE','EEE'),
    ('Mech','Mech'),
    ('Civil','Civil'),
    ('B.Arch','B.Arch'),
    ('General','General'),
]
Category = [
    ('PRE-EVENT','PRE-EVENT'),
    ('GAMING','GAMING'),
    ('M.A.D','M.A.D'),
    ('CLUB','CLUB'),
    ('MISC','MISC'),
    ('TECH','TECH'),
    ('NON-TECH','NON-TECH')
]
filedefault='https://testhttp1234.blob.core.windows.net/media/about-ritu_ft9zmHG.jpg'
descdefault=""
namedefault=""
contactdefault='name:0'
ruledefault=""
class event(models.Model):

    name = models.CharField(max_length=300,default=namedefault)
    description = models.TextField(default=descdefault)
    reglink = models.CharField(max_length=200,default='https://ritu20.com/')
    prize = models.IntegerField(default=0)
    fees = models.CharField(default=0,max_length=200,blank=True,null=True)
    contacts = models.TextField(default=contactdefault) #to easily add text. its JSON
    image = models.FileField(blank=True,null=True)
    ImageFrom = models.ForeignKey(Image,blank=True,null=True,on_delete=models.CASCADE)
    dept = models.CharField(choices=DEPTS,max_length=10,default='General')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rules = models.TextField(blank=True,null=True)
    date = models.CharField(max_length=300,blank=True,null=True)
    time = models.CharField(max_length=300,blank=True,null=True)
    online = models.BooleanField(default=False)
    preevent = models.BooleanField(default=False)
    seats = models.IntegerField(default=1)
    available = models.IntegerField(default=1)
    category = models.CharField(blank=True,null=True,max_length=200,default="Misc",choices=Category)
    createDate = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.createDate = timezone.now()
        return super(event, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class workshop(models.Model):
    name = models.CharField(max_length=300,default=namedefault)
    description = models.TextField(default=descdefault)
    reglink = models.CharField(max_length=200,default='https://ritu20.com/')
    fees = models.CharField(default=0,max_length=200,blank=True,null=True)
    contacts = models.TextField(default=contactdefault)
    image = models.FileField(blank=True,null=True)
    ImageFrom = models.ForeignKey(Image,blank=True,null=True,on_delete=models.CASCADE)
    dept = models.CharField(choices=DEPTS,max_length=10)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.CharField(max_length=300,blank=True,null=True)
    time = models.CharField(max_length=300,blank=True,null=True)
    seats = models.IntegerField(default=1)
    available = models.IntegerField(default=1)
    createDate = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.createDate = timezone.now()
        return super(workshop, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
