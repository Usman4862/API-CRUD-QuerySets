from django.contrib import admin
from .models import *

@admin.register(OppoModel)
class OppoModelAdmin(admin.ModelAdmin):
    list_display= [
        'name', 'model', 'battery', 'screen_size', 
        'created_at', 'updated_at'
    ]