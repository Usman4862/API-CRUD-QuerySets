from django.contrib import admin
from .models import *

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display= [
        'name', 
        'age',
        'city',
        'created_at',
        'updated_at',
    ]