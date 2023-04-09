from django.db import models

class Singer(models.Model):
    class GenderChoice(models.TextChoices):
        MALE = "MALE", "Male",
        FEMALE = "FEMALE", "Female",
        OTHERS = "OTHERS", "Others" 

    first_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GenderChoice.choices, help_text='Please select gender')


    def __str__(self) -> str:
        return self.first_name


class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.PROTECT, related_name='song')
    duration = models.FloatField()


    def __str__(self) -> str:
       return self.title
