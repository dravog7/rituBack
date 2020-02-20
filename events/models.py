from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class event(models.Model):
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
    name = models.CharField(max_length=300)
    description = models.TextField()
    reglink = models.URLField(default='about:blank')
    prize = models.IntegerField()
    contacts = models.TextField() #to easily add text. its JSON
    image = models.ImageField()
    dept = models.CharField(choices=DEPTS,max_length=10)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name