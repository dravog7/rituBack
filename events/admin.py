from django.contrib import admin
from .models import event,workshop
import json
# Register your models here.

def process_rules(txt):
    try:
        obj=json.loads(txt)
        return txt
    except:   
        obj=txt.split("\n")
        return json.dumps(obj)

def process_contacts(txt):
    try:
        obj=json.loads(txt)
        return txt
    except:
        obj=[]
        a=txt.split("\n")
        for i in a:
            b=i.split(":")
            obj.append({"name":b[0].strip(),"mob":b[1].strip()})
        return json.dumps(obj)

@admin.register(event)
class eventAdmin(admin.ModelAdmin):
    exclude = ['user']
    def save_model(self,request,obj,form,change):
        obj.user = request.user
        obj.rules = process_rules(obj.rules)
        obj.contacts = process_contacts(obj.contacts)
        super(eventAdmin,self).save_model(request,obj,form,change)
    
    def get_queryset(self,request):
        qs = super(eventAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user = request.user)

@admin.register(workshop)
class workshopAdmin(admin.ModelAdmin):
    exclude = ['user']
    def save_model(self,request,obj,form,change):
        obj.user = request.user
        obj.contacts = process_contacts(obj.contacts)
        super(workshopAdmin,self).save_model(request,obj,form,change)
    
    def get_queryset(self,request):
        qs = super(workshopAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user = request.user)