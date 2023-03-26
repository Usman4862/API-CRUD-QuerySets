from django.contrib import admin
from .models import TestOne

# Register your models here.
@admin.register(TestOne)
class TestOneAdmin(admin.ModelAdmin):
    list_display= ['name', 'email', 'date_of_birth','created_at', 'updated_at', 'age']


    # def get_queryset(self, obj):
    #     queryset =  super().get_queryset(obj)
    #     queryset = queryset.filter(name__istartswith='a')
    #     return queryset
    

    def get_queryset(self, obj):
        queryset =  super().get_queryset(obj)

        # queryset = queryset.filter(age__gt='2000-02-01').filter(name__istartswith='c')
        # queryset = queryset.filter(created_at__lt='2000-01-01').filter(name__istartswith='c').filter(created_at__lt='date_of_birth')
        # queryset = queryset.filter(email__icontains='org').filter(created_at__gt='2000-01-01')
        # queryset = queryset.filter(id__gt=50).filter(name__icontains='face')
        # queryset = queryset.exclude(id__exact='56')
        # import datetime
        # person_enter = datetime.date(2000, 1, 1)
        # person_leave = datetime.date(2004, 12, 31)
        # sample_dob = datetime.date(2000, 1, 1)
        # queryset = queryset.filter(created_at__range=(person_enter, person_leave)).filter(date_of_birth__gt=sample_dob).filter(updated_at__lt=sample_dob).filter(name__iendswith='r.')
        # queryset = queryset.filter(created_at__year__lt=2000).filter(created_at__month__gt='6')
        # queryset = queryset.filter(date_of_birth__day__lte='5')
        # those persons who updated from monday to friday in time between (12pm to 6pm)
        queryset = queryset.filter(updated_at__week_day__gte='2', updated_at__week_day__lte='6').filter(updated_at__hour__gt='12', updated_at__hour__lt='18')
        

        return queryset


    # def _age(self, obj):
    #     return TestOne.objects.filter(age__lt=2000)
        