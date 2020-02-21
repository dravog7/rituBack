from django.contrib import admin
from .models import event,workshop
# Register your models here.
@admin.register(event)
class eventAdmin(admin.ModelAdmin):
    fields = ['name',
        'description',
        'reglink',
        'prize',
        'contacts',
        'image',
        'rules',
        'dept']
    def save_model(self,request,obj,form,change):
        obj.user = request.user
        super(eventAdmin,self).save_model(request,obj,form,change)
    
    def get_queryset(self,request):
        qs = super(eventAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user = request.user)

@admin.register(workshop)
class workshopAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'description',
        'reglink',
        'fees',
        'contacts',
        'image',
        'dept',
    ]
    def save_model(self,request,obj,form,change):
        obj.user = request.user
        super(workshopAdmin,self).save_model(request,obj,form,change)
    
    def get_queryset(self,request):
        qs = super(workshopAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user = request.user)