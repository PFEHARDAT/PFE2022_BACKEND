from django.db import models
from usersApp.models import User

# Create your models here.


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='User_content')
    subscription = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='Subscription_content')

