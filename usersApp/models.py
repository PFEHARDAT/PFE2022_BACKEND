from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
    
class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


    def get_email(self):
        return self.email