from django.contrib import admin
from .models import *

@admin.register(Sweeper)
class SweeperAdmin(admin.ModelAdmin):
    list_display= [
        'first_name',
        'last_name',
        'date_of_birth',
        'cleaning_frequency',
        'created_at',
        'updated_at', 
    ]
    