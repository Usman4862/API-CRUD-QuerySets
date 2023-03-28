from django.db import models

class Sweeper(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    date_of_birth = models.DateField()
    cleaning_frequency = models.PositiveIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.first_name} - {self.last_name}"
    