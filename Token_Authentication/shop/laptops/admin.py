from django.contrib import admin
from .models import *

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display= [
        'name', 'model', 'company', 'price',
        'hard_drive_size', 'screen_size', 'warrenty'
    ]