from django.contrib import admin
from .models import *

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display= ['first_name', 'last_name', 'city', 'contact']
    