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

def translate_rules(txt):
    try:
        obj = json.loads(txt)
        return "\n".join(obj)
    except:
        return txt

def translate_contacts(txt):
    try:
        obj = json.loads(txt)
        arr = []
        for i in obj:
            arr.append(f"{i['name']}:{i['mob']}")
        return "\n".join(arr)
    except:
        return txt


@admin.register(event)
class eventAdmin(admin.ModelAdmin):
    exclude = ['user']
    list_display = ('name', 'dept','date','category')
    def save_model(self,request,obj,form,change):
        #check image,if null. set as ImageFrom
        if((not obj.image)and(obj.ImageFrom)):
            obj.image=obj.ImageFrom.image
            obj.ImageFrom = None
        obj.user = request.user
        obj.rules = process_rules(obj.rules)
        obj.contacts = process_contacts(obj.contacts)
        super(eventAdmin,self).save_model(request,obj,form,change)
    
    def get_queryset(self,request):
        qs = super(eventAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user = request.user)
    
    def get_object(self, request, object_id,from_field=None):
        obj = super(eventAdmin, self).get_object(request, object_id,from_field=from_field)
        obj.rules = translate_rules(obj.rules)
        obj.contacts = translate_contacts(obj.contacts)
        return obj

@admin.register(workshop)
class workshopAdmin(admin.ModelAdmin):
    exclude = ['user']
    list_display = ('name', 'dept','date')
    def save_model(self,request,obj,form,change):
        #check image,if null. set as ImageFrom
        if((not obj.image)and(obj.ImageFrom)):
            obj.image=obj.ImageFrom.image
        obj.user = request.user
        obj.contacts = process_contacts(obj.contacts)
        super(workshopAdmin,self).save_model(request,obj,form,change)
    
    def get_queryset(self,request):
        qs = super(workshopAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user = request.user)
    
    def get_object(self, request, object_id,from_field=None):
        obj = super(workshopAdmin, self).get_object(request, object_id,from_field=from_field)
        obj.contacts = translate_contacts(obj.contacts)
        return obj