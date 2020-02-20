from django.contrib import admin
from .models import event
# Register your models here.
@admin.register(event)
class eventAdmin(admin.ModelAdmin):
    def save_model(self,request,obj,form,change):
        obj.user = request.user
        super(eventAdmin,self).save_model(request,obj,form,change)
    
    def get_queryset(self,request):
        qs = super(eventAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user = request.user)