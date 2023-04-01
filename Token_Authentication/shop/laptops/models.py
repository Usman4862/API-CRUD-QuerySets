from django.db import models



class Laptop(models.Model):
    class WarrentyChoice(models.TextChoices):
        SIX_MONTH = '6M', '6_Month',
        TWELVE_MONTH = '12M', '12_Month',
        EIGHTEEN_MONTH = '18M', '18_Month',
    

    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    price = models.BigIntegerField(help_text='Price in Dollars $')
    hard_drive_size = models.CharField(max_length=50)
    screen_size = models.SmallIntegerField(help_text='Size in inches')
    warrenty = models.CharField(max_length=50, choices=WarrentyChoice.choices)


