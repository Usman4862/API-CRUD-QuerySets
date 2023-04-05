from django.db import models


class FakeThrottle(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.name}"
    

