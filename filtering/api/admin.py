from django.contrib import admin
from .models import SampleModel


@admin.register(SampleModel)
class SampleModelAdmin(admin.ModelAdmin):
    list_display= ['movie', 'category', 'series', 'phone_number']
    save_as=True
