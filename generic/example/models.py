from django.db import models

class ExampleModel(models.Model):
    class CityChoice(models.TextChoices):
        FAISALABAD = "F", ("Faisalabad"),
        ISLAMABAD = "I", ("Islamabad"),
        LONDON = "L", ("London"),

    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=50, choices=CityChoice.choices, null=False, blank=False)
    contact = models.PositiveIntegerField(help_text="Please Enter 12 digits Contact Number")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    short_bio = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} - {self.last_name}"
