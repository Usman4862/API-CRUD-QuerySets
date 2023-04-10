from django.contrib import admin
from .models import Sample

@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display= [
        'first_name',
        'city',
        'roll',
    ]