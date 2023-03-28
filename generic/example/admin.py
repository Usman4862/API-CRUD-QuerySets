from django.contrib import admin
from .models import *

@admin.register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    list_display= ['first_name', 'last_name', 'city', 'contact', 'created_at', 'updated_at']
    save_as=True
    