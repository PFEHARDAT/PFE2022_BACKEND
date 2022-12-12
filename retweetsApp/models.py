from django.db import models
from usersApp.models import User
# import post
# Create your models here.


class Retweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='retweet_user_content')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_content')
    class Meta:
        db_table = 'retweetsApp_retweet'
        unique_together = ('user', 'post')