from django.db import models
from django.contrib.auth.models import User


class OppoModel(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50, verbose_name='Mobile Model')
    battery = models.CharField(max_length=50)
    screen_size = models.CharField(
        max_length=50, help_text='Please Enter size in inches.', null=True
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, parent_link=True)
    created_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)


    def __str__(self) -> str:
        return f"{self.name}-{self.model}"
    