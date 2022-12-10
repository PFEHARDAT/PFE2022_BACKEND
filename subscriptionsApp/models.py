from django.db import models
from usersApp.models import User

# Create your models here.


class Subscription(models.Model):
    user = models.ForeignKey(User)
    subscription = models.ForeignKey(User)

