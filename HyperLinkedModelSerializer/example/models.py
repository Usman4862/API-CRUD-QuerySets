from django.db import models


class Sample(models.Model):
    first_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    roll = models.IntegerField()


    def __str__(self) -> str:
        return self.first_name