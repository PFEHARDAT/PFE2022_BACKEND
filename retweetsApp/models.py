from django.db import models
from usersApp.models import User
from postsApp.models import Post
# import post
# Create your models here.


class Retweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='retweet_user_content')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_content')
    retweet_date = models.DateTimeField(auto_now_add = True, auto_now = False) 

    class Meta:
        db_table = 'retweetsApp_retweet'
        unique_together = ('user', 'post')
    
    