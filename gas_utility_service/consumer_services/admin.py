from django.contrib import admin
from consumer_services.models import *
# Register your models here.
# class requestadmin(admin.ModelAdmin):
#     list_display=['shoename','detail','price','cat','is_active']

# admin.site.register(ServiceRequest,requestadmin)
from .models import ServiceRequest

admin.site.register(ServiceRequest)
