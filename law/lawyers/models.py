from django.db import models
from django.contrib.auth.models import AbstractUser

class Lawyers(AbstractUser):
    phone_number = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.username}"   
