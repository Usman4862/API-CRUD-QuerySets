from django.contrib import admin
from .models import *

@admin.register(OppoModel)
class OppoModelAdmin(admin.ModelAdmin):
    list_display= [
        'first_name',
        'last_name',
        'model',
        'battery',
        'screen_size', 
        'created_at',
        'updated_at'
    ]
    exclude= ['created_at', 'updated_at']

