from django.db import models
from .choice import GENDER_CHOICE

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=1)
    age = models.PositiveSmallIntegerField()
    favorite_number = models.PositiveSmallIntegerField()  # Fixed typo
    created = models.DateField(auto_now_add=True)

    def __str__(self):  # Fixed method name
        return f"{self.name} (ID: {self.id})"  # Properly formatted string
