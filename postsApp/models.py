from django.db import models
from usersApp.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.CharField(max_length= 300)
    publication_date = models.DateTimeField(auto_now_add = True, auto_now = False) 
    like_count = models.BigIntegerField()
    comment_count = models.BigIntegerField()
    retweet_count = models.BigIntegerField()
    is_comment = models.BooleanField(default=False)
    response_to_post = models.ForeignKey('self', on_delete = models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.content

