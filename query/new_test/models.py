from django.db import models


class TestOne(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField()    
    age = models.DateField(null=True)
    email = models.EmailField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}"

    