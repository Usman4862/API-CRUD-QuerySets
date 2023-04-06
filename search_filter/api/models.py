from django.db import models


class SampleModel(models.Model):
    movie = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11, null=True, help_text='Please Enter 11 Digits Phone Number')
    




