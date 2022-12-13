from django.db import models
from usersApp.models import User


# Create your models here.


class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_user_content')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_content')
    class Meta:
        db_table = 'followersApp_follower'
        unique_together = ('user', 'follower')