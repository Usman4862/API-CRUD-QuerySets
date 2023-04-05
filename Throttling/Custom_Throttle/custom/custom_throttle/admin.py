from django.contrib import admin
from .models import *

@admin.register(FakeThrottle)
class FakeThrottleAdmin(admin.ModelAdmin):
    list_display= [
        'name',
        'city',
        'age',
    ]



    # def get_queryset(self, obj):
    #     queryset = super().get_queryset(obj)
    #     queryset = queryset.filter(age__lt='1000').exclude(city__iexact='lkkl')
    #     return queryset